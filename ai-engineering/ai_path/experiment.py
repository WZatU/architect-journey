"""P01: grouped telemetry classification with validation-only model selection.

All examples are generated from a fictional simulator. Results describe this
generator, not a deployed robot or a validated physical safety classifier.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import numpy as np
import sklearn
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, brier_score_loss, confusion_matrix, f1_score
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def make_telemetry(seed: int = 17, devices: int = 60, runs: int = 12):
    """Generate features without using the target as an input feature."""
    if devices < 15 or runs < 2:
        raise ValueError("at least 15 devices and 2 runs are required")
    rng = np.random.default_rng(seed)
    records = []
    for device in range(devices):
        bias = rng.normal(0, 0.2)
        for run in range(runs):
            unstable = int(rng.random() < 0.35)
            records.append({
                "device": device,
                "run": run,
                "speed": float(rng.normal(0.8 - 0.15 * unstable + bias, 0.2)),
                "acceleration_variance": float(rng.lognormal(-0.8 + unstable, 0.6)),
                "tracking_error": float(rng.lognormal(-1.5 + 1.3 * unstable + bias, 0.5)),
                "temperature": float(rng.normal(38 + 3 * unstable + bias, 3)),
                "target": unstable,
            })
    return records


FEATURES = ["speed", "acceleration_variance", "tracking_error", "temperature"]


def grouped_split(groups, seed=17):
    indices = np.arange(len(groups))
    outer = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=seed)
    trainval, test = next(outer.split(indices, groups=groups))
    inner = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=seed + 1)
    train_part, val_part = next(inner.split(trainval, groups=groups[trainval]))
    train, val = trainval[train_part], trainval[val_part]
    partitions = [set(groups[x]) for x in (train, val, test)]
    if any(partitions[i] & partitions[j] for i in range(3) for j in range(i)):
        raise ValueError("device leakage between partitions")
    return train, val, test


def grouped_bootstrap_accuracy(y, pred, groups, seed=17, repetitions=300):
    """Resample devices, preserving within-device dependence."""
    rng = np.random.default_rng(seed)
    unique = np.unique(groups)
    scores = []
    for _ in range(repetitions):
        chosen = rng.choice(unique, size=len(unique), replace=True)
        idx = np.concatenate([np.flatnonzero(groups == group) for group in chosen])
        scores.append(float(np.mean(y[idx] == pred[idx])))
    return [float(x) for x in np.quantile(scores, [0.025, 0.975])]


def run_experiment(seed=17):
    records = make_telemetry(seed)
    x = np.asarray([[row[k] for k in FEATURES] for row in records])
    y = np.asarray([row["target"] for row in records])
    groups = np.asarray([row["device"] for row in records])
    train, val, test = grouped_split(groups, seed)
    trials = []
    for c in (0.1, 1.0, 10.0):
        candidate = make_pipeline(StandardScaler(), LogisticRegression(C=c, max_iter=300))
        candidate.fit(x[train], y[train])
        score = float(f1_score(y[val], candidate.predict(x[val]), average="macro"))
        trials.append({"C": c, "validation_macro_f1": score})
    best = max(trials, key=lambda row: row["validation_macro_f1"])
    final_train = np.concatenate([train, val])
    model = make_pipeline(StandardScaler(), LogisticRegression(C=best["C"], max_iter=300))
    model.fit(x[final_train], y[final_train])
    baseline = DummyClassifier(strategy="prior").fit(x[final_train], y[final_train])
    pred, base_pred = model.predict(x[test]), baseline.predict(x[test])
    prob = model.predict_proba(x[test])[:, 1]
    digest = hashlib.sha256(json.dumps(records, sort_keys=True).encode()).hexdigest()
    return {
        "project": "P01", "measurement_origin": "local_cpu_measured",
        "dataset": "original synthetic telemetry; physical validity not established",
        "seed": seed, "data_sha256": digest, "features": FEATURES,
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scikit_learn": sklearn.__version__},
        "split": {name: {"rows": len(idx), "devices": sorted(set(groups[idx].tolist()))}
                  for name, idx in [("train", train), ("validation", val), ("test", test)]},
        "validation_trials": trials, "selected_C": best["C"],
        "test": {
            "accuracy": float(accuracy_score(y[test], pred)),
            "macro_f1": float(f1_score(y[test], pred, average="macro")),
            "baseline_macro_f1": float(f1_score(y[test], base_pred, average="macro")),
            "brier_score": float(brier_score_loss(y[test], prob)),
            "confusion_matrix": confusion_matrix(y[test], pred, labels=[0, 1]).tolist(),
            "device_bootstrap_accuracy_ci95": grouped_bootstrap_accuracy(
                y[test], pred, groups[test], seed),
            "errors": [{"row_index": int(i), "device": int(groups[i]),
                        "expected": int(y[i]), "predicted": int(p)}
                       for i, p in zip(test, pred) if y[i] != p],
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument("--output", type=Path, default=Path("outputs/p01.json"))
    args = parser.parse_args()
    result = run_experiment(args.seed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"output": str(args.output), "test": result["test"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
