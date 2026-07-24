#!/usr/bin/env python3
"""Read a robot position CSV and write velocity/acceleration statistics to JSON.

Expected CSV shape (column names are configurable):

    time,x,y,z
    0.0,0.0,0.0,0.0
    0.1,0.2,0.0,0.0

Velocity is the finite difference between adjacent position samples. Acceleration
is the finite difference between adjacent velocity samples. Statistics use the
population variance (divide by N).
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from pathlib import Path


TIME_CANDIDATES = ("time", "timestamp", "t")
POSITION_CANDIDATES = (
    ("x", "y", "z"),
    ("position_x", "position_y", "position_z"),
    ("pos_x", "pos_y", "pos_z"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute robot velocity, acceleration, mean, and variance."
    )
    parser.add_argument("input_csv", type=Path, help="robot test CSV")
    parser.add_argument("output_json", type=Path, help="destination JSON")
    parser.add_argument("--time-column", help="time column (auto-detected by default)")
    parser.add_argument(
        "--position-columns",
        nargs="+",
        help="position columns, for example: --position-columns x y z",
    )
    return parser.parse_args()


def detect_columns(
    fieldnames: list[str], requested_time: str | None, requested_positions: list[str] | None
) -> tuple[str, list[str]]:
    time_column = requested_time or next(
        (name for name in TIME_CANDIDATES if name in fieldnames), None
    )
    if time_column is None:
        raise ValueError(
            f"Cannot find a time column. Available columns: {', '.join(fieldnames)}"
        )

    if requested_positions:
        position_columns = requested_positions
    else:
        position_columns = next(
            ([name for name in group if name in fieldnames] for group in POSITION_CANDIDATES
             if any(name in fieldnames for name in group)),
            [],
        )
    missing = [name for name in [time_column, *position_columns] if name not in fieldnames]
    if missing:
        raise ValueError(f"Missing CSV columns: {', '.join(missing)}")
    if not position_columns:
        raise ValueError(
            "Cannot detect position columns. Supply them with --position-columns."
        )
    return time_column, position_columns


def read_samples(
    path: Path, time_column: str | None, position_columns: list[str] | None
) -> tuple[str, list[str], list[dict[str, float]]]:
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames:
            raise ValueError("CSV has no header row")
        selected_time, selected_positions = detect_columns(
            reader.fieldnames, time_column, position_columns
        )
        samples = []
        for line_number, row in enumerate(reader, start=2):
            try:
                sample = {selected_time: float(row[selected_time])}
                sample.update({name: float(row[name]) for name in selected_positions})
            except (TypeError, ValueError) as error:
                raise ValueError(f"Non-numeric or empty value on CSV line {line_number}") from error
            samples.append(sample)

    if len(samples) < 3:
        raise ValueError("At least 3 samples are required to compute acceleration")
    return selected_time, selected_positions, samples


def vector_differences(
    samples: list[dict[str, float]], time_key: str, value_keys: list[str]
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for previous, current in zip(samples, samples[1:]):
        dt = current[time_key] - previous[time_key]
        if dt <= 0:
            raise ValueError("Time values must be strictly increasing")
        vector = {
            key: (current[key] - previous[key]) / dt
            for key in value_keys
        }
        results.append(
            {
                "time": (previous[time_key] + current[time_key]) / 2,
                "dt": dt,
                "vector": vector,
                "magnitude": math.sqrt(sum(value * value for value in vector.values())),
            }
        )
    return results


def acceleration_from_velocity(
    velocities: list[dict[str, object]], position_keys: list[str]
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for previous, current in zip(velocities, velocities[1:]):
        previous_time = float(previous["time"])
        current_time = float(current["time"])
        dt = current_time - previous_time
        previous_vector = previous["vector"]
        current_vector = current["vector"]
        assert isinstance(previous_vector, dict) and isinstance(current_vector, dict)
        vector = {
            key: (float(current_vector[key]) - float(previous_vector[key])) / dt
            for key in position_keys
        }
        results.append(
            {
                "time": (previous_time + current_time) / 2,
                "dt": dt,
                "vector": vector,
                "magnitude": math.sqrt(sum(value * value for value in vector.values())),
            }
        )
    return results


def stats(records: list[dict[str, object]], keys: list[str]) -> dict[str, object]:
    axis_stats = {}
    for key in keys:
        values = [float(record["vector"][key]) for record in records]  # type: ignore[index]
        axis_stats[key] = {
            "mean": statistics.fmean(values),
            "variance": statistics.pvariance(values),
        }
    magnitudes = [float(record["magnitude"]) for record in records]
    return {
        "by_axis": axis_stats,
        "magnitude": {
            "mean": statistics.fmean(magnitudes),
            "variance": statistics.pvariance(magnitudes),
        },
    }


def main() -> None:
    args = parse_args()
    time_key, position_keys, samples = read_samples(
        args.input_csv, args.time_column, args.position_columns
    )
    velocities = vector_differences(samples, time_key, position_keys)
    accelerations = acceleration_from_velocity(velocities, position_keys)
    output = {
        "source": str(args.input_csv),
        "method": {
            "derivative": "finite difference between adjacent samples",
            "variance": "population variance (divide by N)",
        },
        "columns": {"time": time_key, "position": position_keys},
        "sample_count": len(samples),
        "velocity": {"records": velocities, "statistics": stats(velocities, position_keys)},
        "acceleration": {
            "records": accelerations,
            "statistics": stats(accelerations, position_keys),
        },
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {args.output_json}")


if __name__ == "__main__":
    main()
