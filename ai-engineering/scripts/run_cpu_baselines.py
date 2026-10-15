"""Run from ai-engineering/: python scripts/run_cpu_baselines.py."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
COMMANDS = [
    ['-m', 'ai_path.experiment'],
    ['-m', 'ai_path.retrieval'],
    ['-m', 'ai_path.workflow'],
    ['-m', 'ai_path.trace_metrics', '--input', 'data/inference-fixture.jsonl'],
]

if __name__ == '__main__':
    for command in COMMANDS:
        result = subprocess.run([sys.executable, *command], cwd=ROOT, check=True, capture_output=True, text=True)
        print(json.dumps({'command':command,'status':'passed','output_tail':result.stdout[-350:]}))
