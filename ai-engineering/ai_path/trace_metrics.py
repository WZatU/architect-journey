"""P06: analyze per-token traces without inventing GPU measurements."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from statistics import mean


def summarize(rows: list[dict]) -> dict:
    if not rows:
        raise ValueError("traces cannot be empty")
    ttft, tpot, totals = [], [], []
    token_count = 0
    origins = set()
    for row in rows:
        origin = row.get("measurement_origin")
        if origin not in {"fixture", "measured"}:
            raise ValueError("measurement_origin must be explicit")
        origins.add(origin)
        start, end = row["start_s"], row["end_s"]
        times = row["token_times_s"]
        values = [start, end, *times]
        if not times or any(type(x) not in {int, float} or not math.isfinite(x) for x in values):
            raise ValueError("finite timestamps and at least one token are required")
        if start > times[0] or times[-1] > end or any(a > b for a, b in zip(times, times[1:])):
            raise ValueError("timestamps must be ordered")
        if end <= start:
            raise ValueError("duration must be positive")
        if type(row["output_tokens"]) is not int or len(times) != row["output_tokens"]:
            raise ValueError("token count must match timestamp count")
        ttft.append(times[0] - start)
        totals.append(end - start)
        if len(times) > 1:
            tpot.append((times[-1] - times[0]) / (len(times) - 1))
        token_count += len(times)
    if len(origins) != 1:
        raise ValueError("do not mix fixture and measured traces")
    wall_time = max(row["end_s"] for row in rows) - min(row["start_s"] for row in rows)
    return {"measurement_origin": origins.pop(), "requests": len(rows),
            "mean_ttft_s": mean(ttft), "mean_tpot_s": mean(tpot) if tpot else None,
            "mean_e2e_s": mean(totals), "output_tokens": token_count,
            "output_tokens_per_wall_second": token_count / wall_time,
            "note": "TPOT excludes first-token delay; fixture values are not hardware results"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("outputs/p06-fixture.json"))
    args = parser.parse_args()
    rows = [json.loads(line) for line in args.input.read_text().splitlines() if line.strip()]
    result = summarize(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
