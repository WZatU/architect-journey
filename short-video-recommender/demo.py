"""Run: python demo.py [--interactive] [--user 0] [--seed 42]."""

import argparse
import csv
from dataclasses import asdict
import json
from pathlib import Path

import numpy as np

from recommender import (Event, FEATURE_NAMES, Ranker, TOPICS, evaluate, make_data,
                         popularity, recommend, training_examples, user_profile)


def experiment(seed=42, epochs=500):
    videos, events = make_data(seed=seed)
    x, y, users = training_examples(videos, events)
    train_end, val_end = int(0.6 * len(events)), int(0.8 * len(events))
    model, training = Ranker.fit(x[:train_end], y[:train_end],
                                 x[train_end:val_end], y[train_end:val_end], epochs=epochs)
    # Both baselines have access to training labels only, just like the ranker.
    global_p = np.broadcast_to(y[:train_end].mean(axis=0), y[val_end:].shape)
    topic_positives, topic_counts = np.ones((len(TOPICS), 2)), np.full(len(TOPICS), 2.0)
    for event, labels in zip(events[:train_end], y[:train_end]):
        topic = videos[event.video_id].topic
        topic_positives[topic] += labels
        topic_counts[topic] += 1
    topic_rates = topic_positives / topic_counts[:, None]
    topic_p = np.asarray([topic_rates[videos[e.video_id].topic] for e in events[val_end:]])
    test_y, test_users = y[val_end:], users[val_end:]
    metrics = {
        "seed": seed, "data_kind": "synthetic_uniform_random_exposures",
        "users": len(set(users.tolist())), "videos": len(videos),
        "train_rows": train_end, "validation_rows": val_end - train_end,
        "test_rows": len(events) - val_end,
        "last_train_timestamp": events[train_end - 1].timestamp,
        "first_validation_timestamp": events[train_end].timestamp,
        "last_validation_timestamp": events[val_end - 1].timestamp,
        "first_test_timestamp": events[val_end].timestamp,
        "evaluation": "chronological, frozen weights, prefix-only profiles; logged candidates",
        "global_baseline": evaluate(test_y, global_p, test_users),
        "topic_baseline": evaluate(test_y, topic_p, test_users),
        "personalized_ranker": evaluate(test_y, model.predict(x[val_end:]), test_users),
        "training": training,
    }
    return videos, events, model, popularity(videos, events[:train_end]), metrics


def save_outputs(out, videos, events, model, metrics, recommendations):
    out.mkdir(parents=True, exist_ok=True)
    for name, rows in (("videos", videos), ("events", events)):
        with (out / f"{name}.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0])))
            writer.writeheader()
            writer.writerows(asdict(row) for row in rows)
    payloads = {"metrics.json": metrics,
                "model.json": {"feature_names": FEATURE_NAMES, "heads": ["complete", "like"],
                               "weights": model.weights.tolist()},
                "recommendations.json": recommendations}
    for name, payload in payloads.items():
        (out / name).write_text(json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False)
                               + "\n", encoding="utf-8")


def show_feed(rows):
    print("\nID    topic        seconds  P(>=80%)  P(like)  mode")
    for row in rows:
        mode = "explore" if row["exploration"] else "ranked"
        print(f'{row["video_id"]:<5} {row["topic"]:<12} {row["duration_s"]:<8}'
              f'{row["p_complete"]:.3f}     {row["p_like"]:.3f}    {mode}')
    if rows:
        print("Next:", rows[0]["title"])


def interactive(model, videos, history, popular, user, seed, out, next_timestamp):
    print("\n交互演示使用虚构视频标题，不播放视频。")
    print("w=看完，l=看完并点赞，s=立即划走，0~1=观看比例，q=退出。")
    print("每次只反馈第一条；未观看的预览不会写入历史。兴趣更新，全局模型权重固定。")
    # A separate log per run keeps old feedback and avoids ambiguous replay across seeds.
    from datetime import datetime, timezone
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    feedback_path = out / f"feedback-{stamp}.jsonl"
    print(f"本次反馈: {feedback_path}（下次运行不会自动导入）")
    turn = 0
    while True:
        rows = recommend(model, videos, history, popular, seed=seed + turn)
        if not rows:
            print("所有视频都已看过。")
            break
        show_feed(rows)
        try:
            action = input("反馈 > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if action == "q":
            break
        try:
            ratio = {"w": 1.0, "l": 1.0, "s": 0.03}.get(action)
            ratio = float(action) if ratio is None else ratio
            event = Event(next_timestamp + turn, user, rows[0]["video_id"], ratio, action == "l")
        except ValueError:
            print("请输入 w / l / s / q 或 0~1 的数字。")
            continue
        history.append(event)
        with feedback_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(event)) + "\n")
        turn += 1
        profile = user_profile(history, videos)
        print("兴趣占比:", "  ".join(f"{topic}={value:.0%}" for topic, value in zip(TOPICS, profile)))


def main():
    parser = argparse.ArgumentParser(description="A minimal short-video recommendation lab")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--user", type=int, default=0, help="0..119 = existing user; other IDs = cold start")
    parser.add_argument("--epochs", type=int, default=500)
    parser.add_argument("--out", type=Path, default=Path("artifacts"))
    parser.add_argument("--interactive", action="store_true")
    args = parser.parse_args()
    if args.epochs < 1:
        parser.error("--epochs must be positive")
    videos, events, model, popular, metrics = experiment(args.seed, args.epochs)
    history = [event for event in events if event.user_id == args.user]
    rows = recommend(model, videos, history, popular, seed=args.seed)
    save_outputs(args.out, videos, events, model, metrics, rows)
    print("Synthetic data only | chronological train/validation/test = 60/20/20")
    print("method                complete AUC   like AUC    logged NDCG@10")
    for name in ("global_baseline", "topic_baseline", "personalized_ranker"):
        result = metrics[name]
        print(f'{name:<22}{result["complete_auc"]:.4f}         {result["like_auc"]:.4f}'
              f'      {result["logged_ndcg@10"]:.4f}')
    print(f'Best validation epoch: {metrics["training"]["best_epoch"]}')
    print(f"User {args.user}: {len(history)} past exposures | outputs: {args.out}")
    if args.interactive:
        interactive(model, videos, history, popular, args.user, args.seed, args.out,
                    events[-1].timestamp + 1)
    else:
        show_feed(rows)


if __name__ == "__main__":
    main()
