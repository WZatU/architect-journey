"""A small, inspectable short-video recommender. Python 3.10+ and NumPy only."""

from dataclasses import dataclass
import math

import numpy as np

TOPICS = ("AI", "math", "piano", "cooking", "basketball", "travel")
FEATURE_NAMES = ("bias", "interest_match", "duration_minutes", *TOPICS)


@dataclass(frozen=True)
class Video:
    video_id: int
    topic: int
    duration_s: int
    title: str


@dataclass(frozen=True)
class Event:
    timestamp: int
    user_id: int
    video_id: int
    watch_ratio: float
    liked: bool

    def __post_init__(self):
        if not math.isfinite(self.watch_ratio) or not 0 <= self.watch_ratio <= 1:
            raise ValueError("watch_ratio must be finite and between 0 and 1")


def sigmoid(x):
    # tanh avoids overflowing exp for large positive or negative logits.
    return 0.5 * (1.0 + np.tanh(np.asarray(x) / 2.0))


def make_data(seed=42, n_users=120, n_videos=600, steps=120):
    """Random exposures; hidden tastes generate labels, never model features."""
    if n_users < 1 or not 1 <= steps <= n_videos or n_videos < len(TOPICS):
        raise ValueError("need users >= 1, videos >= 6, and 1 <= steps <= videos")
    rng = np.random.default_rng(seed)
    titles = ("Build a tiny agent", "A probability puzzle", "Chopin practice",
              "Make tomato eggs", "A shooting drill", "A lakeside walk")
    videos = [Video(i, i % len(TOPICS), int(rng.integers(10, 61)),
                    f"{titles[i % len(TOPICS)]} #{i}") for i in range(n_videos)]
    # These variables exist only inside the simulator, not in the returned data.
    tastes = rng.dirichlet(np.full(len(TOPICS), 0.25), size=n_users)
    quality = rng.normal(0, 0.5, n_videos)
    exposures = [rng.choice(n_videos, steps, replace=False) for _ in range(n_users)]
    events = []
    for step in range(steps):
        for user in range(n_users):
            video = videos[int(exposures[user][step])]
            affinity = len(TOPICS) * tastes[user, video.topic]
            p_complete = sigmoid(-1.6 + 1.25 * affinity
                                 - 0.6 * video.duration_s / 60 + quality[video.video_id])
            complete = rng.random() < p_complete
            ratio = float(rng.uniform(0.8, 1.0) if complete else rng.uniform(0.02, 0.79))
            p_like = sigmoid(-3.2 + 1.05 * affinity + 0.3 * quality[video.video_id])
            liked = bool(rng.random() < p_like and ratio > 0.3)
            events.append(Event(step * n_users + user, user, video.video_id, ratio, liked))
    return videos, events


def user_profile(history, videos):
    """Hand-designed state update: completion/like adds evidence, skips subtract it."""
    evidence = np.full(len(TOPICS), 0.5)
    for age, event in enumerate(reversed(history)):
        reward = 2 * event.watch_ratio - 1 + 1.5 * event.liked
        evidence[videos[event.video_id].topic] += 0.97 ** age * reward
    evidence = np.maximum(evidence, 0.05)
    return evidence / evidence.sum()


def features(profile, video):
    x = np.zeros(len(FEATURE_NAMES))
    x[:3] = (1, len(TOPICS) * profile[video.topic], video.duration_s / 60)
    x[3 + video.topic] = 1
    return x


def training_examples(videos, events):
    """Build features BEFORE adding the current outcome. Global chronological order."""
    histories, xs, ys, users = {}, [], [], []
    ordered = sorted(events, key=lambda e: e.timestamp)
    if len({e.timestamp for e in ordered}) != len(ordered):
        raise ValueError("timestamps must be unique to define a strict event order")
    for event in ordered:
        history = histories.setdefault(event.user_id, [])
        xs.append(features(user_profile(history, videos), videos[event.video_id]))
        ys.append((event.watch_ratio >= 0.8, event.liked))
        users.append(event.user_id)
        history.append(event)
    if not xs:
        raise ValueError("events cannot be empty")
    return np.asarray(xs), np.asarray(ys, dtype=float), np.asarray(users)


def log_loss_from_logits(y, logits):
    return float(np.mean(np.logaddexp(0, logits) - y * logits))


class Ranker:
    """Two independent logistic regressions: P(complete) and P(like)."""

    def __init__(self, weights):
        self.weights = np.asarray(weights, dtype=float)

    def predict(self, x):
        return sigmoid(x @ self.weights)

    @classmethod
    def fit(cls, x, y, x_val, y_val, epochs=500, lr=0.15, l2=0.001):
        if epochs < 1:
            raise ValueError("epochs must be positive")
        weights = np.zeros((x.shape[1], y.shape[1]))
        best_weights, best_loss, best_epoch = weights.copy(), float("inf"), 0
        curve = []
        for epoch in range(1, epochs + 1):
            # Each head minimizes mean BCE + L2. Do not regularize the intercept.
            penalty = weights.copy()
            penalty[0] = 0
            gradient = x.T @ (sigmoid(x @ weights) - y) / len(x) + l2 * penalty
            weights -= lr * gradient
            val_loss = log_loss_from_logits(y_val, x_val @ weights)
            if val_loss < best_loss:
                best_loss, best_epoch, best_weights = val_loss, epoch, weights.copy()
            if epoch == 1 or epoch % 50 == 0 or epoch == epochs:
                curve.append({"epoch": epoch, "train_log_loss": log_loss_from_logits(y, x @ weights),
                              "validation_log_loss": val_loss})
        return cls(best_weights), {"best_epoch": best_epoch, "curve": curve}


def popularity(videos, events):
    """Smoothed completion rate per video, using TRAINING feedback only."""
    positives, counts = np.ones(len(videos)), np.full(len(videos), 2.0)
    for event in events:
        positives[event.video_id] += event.watch_ratio >= 0.8
        counts[event.video_id] += 1
    return positives / counts


def recall(history, videos, popular, rng, limit=80):
    """Union of interest, popularity, and random channels; already-seen IDs excluded."""
    seen = {event.video_id for event in history}
    available = np.asarray([v.video_id for v in videos if v.video_id not in seen], dtype=int)
    if not len(available):
        return []
    profile = user_profile(history, videos)
    shuffled = rng.permutation(available)  # Random tie breaks among same-topic videos.
    interest = sorted(shuffled, key=lambda i: profile[videos[i].topic], reverse=True)
    hot = sorted(shuffled, key=lambda i: popular[i], reverse=True)
    # Deduplication can make the union smaller than the requested budget.
    half, quarter = max(1, limit // 2), max(1, limit // 4)
    return list(dict.fromkeys(int(i) for i in
                             [*interest[:half], *hot[:quarter], *shuffled[:quarter]]))[:limit]


def recommend(model, videos, history, popular, k=10, seed=42,
              exploration=0.1, diversity_penalty=0.12):
    """Rank a recalled pool, penalize topic repetition, randomly insert exploration."""
    if k < 0 or not 0 <= exploration <= 1 or diversity_penalty < 0:
        raise ValueError("invalid k, exploration, or diversity_penalty")
    if not k:
        return []
    rng = np.random.default_rng(seed)
    candidates = recall(history, videos, popular, rng, limit=max(80, 2 * k))
    seen = {e.video_id for e in history}
    available = [v.video_id for v in videos if v.video_id not in seen]
    k = min(k, len(available))
    explore_slots = math.ceil(k * exploration)
    profile = user_profile(history, videos)
    predictions = {i: model.predict(features(profile, videos[i])) for i in candidates}
    chosen, topic_counts = [], np.zeros(len(TOPICS), dtype=int)

    def append(video_id, explore):
        p_complete, p_like = model.predict(features(profile, videos[video_id]))
        video = videos[video_id]
        score = float(0.7 * p_complete + 0.3 * p_like)
        chosen.append({"video_id": video_id, "title": video.title, "topic": TOPICS[video.topic],
                       "duration_s": video.duration_s, "p_complete": float(p_complete),
                       "p_like": float(p_like), "score": score,
                       "adjusted_score": score - diversity_penalty * topic_counts[video.topic],
                       "exploration": explore})
        topic_counts[video.topic] += 1

    explore_positions = set(rng.choice(k, size=explore_slots, replace=False).tolist())
    for position in range(k):
        explore = position in explore_positions or not candidates
        if explore:
            best = int(rng.choice(available))
        else:
            best = max(candidates, key=lambda i: float(predictions[i] @ np.array([0.7, 0.3]))
                       - diversity_penalty * topic_counts[videos[i].topic])
        append(best, explore)
        available.remove(best)
        if best in candidates:
            candidates.remove(best)
    return chosen


def auc(y, scores):
    """Mann-Whitney ROC AUC with average ranks for tied scores; None if undefined."""
    y, scores = np.asarray(y, dtype=bool), np.asarray(scores)
    positives = int(y.sum())
    negatives = len(y) - positives
    if not positives or not negatives:
        return None
    _, inverse, counts = np.unique(scores, return_inverse=True, return_counts=True)
    ranks = (np.cumsum(counts) - counts + 1 + np.cumsum(counts)) / 2
    return float((ranks[inverse][y].sum() - positives * (positives + 1) / 2)
                 / (positives * negatives))


def evaluate(y, probabilities, users, k=10):
    """Frozen-model metrics on logged exposures, not full-catalog retrieval quality."""
    result = {}
    for head, name in enumerate(("complete", "like")):
        p = np.clip(probabilities[:, head], 1e-12, 1 - 1e-12)
        labels = y[:, head]
        result[name + "_auc"] = auc(labels, p)
        result[name + "_log_loss"] = float(-np.mean(labels * np.log(p) + (1-labels)*np.log1p(-p)))
    relevance, scores = y @ np.array([0.7, 0.3]), probabilities @ np.array([0.7, 0.3])
    ndcgs = []
    for user in np.unique(users):
        mask = users == user
        gains = np.expm1(np.log(2) * relevance[mask])
        order = np.argsort(-scores[mask], kind="stable")[:k]
        discounts = 1 / np.log2(np.arange(2, len(order) + 2))
        ideal = np.sort(gains)[::-1][:k] @ discounts
        ndcgs.append(float(gains[order] @ discounts / ideal) if ideal else 0.0)
    result[f"logged_ndcg@{k}"] = float(np.mean(ndcgs))
    return result
