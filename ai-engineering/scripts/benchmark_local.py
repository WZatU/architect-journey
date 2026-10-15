"""Measure the local P04 HTTP adapter, not an LLM or GPU serving system."""
from concurrent.futures import ThreadPoolExecutor
import argparse
import json
from pathlib import Path
import platform
import statistics
import sys
import threading
from time import perf_counter
from urllib.error import HTTPError
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ai_path.service import make_server


def quantile(values, fraction):
    ordered = sorted(values)
    index = (len(ordered) - 1) * fraction
    low = int(index)
    high = min(low + 1, len(ordered) - 1)
    return ordered[low] + (ordered[high] - ordered[low]) * (index - low)


def benchmark(requests=40, workers=4):
    if not 1 <= requests <= 10000 or not 1 <= workers <= 32:
        raise ValueError('requests in [1,10000], workers in [1,32]')
    server = make_server(port=0, credentials={'benchmark-token':'demo'}, max_inflight=workers)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    url = f'http://127.0.0.1:{server.server_port}/v1/search'
    payload = json.dumps({'query':'command retries timeout', 'k':3}).encode()

    def one(request_id):
        req = Request(url, data=payload, headers={'Authorization':'Bearer benchmark-token',
                                                'Content-Type':'application/json'})
        start = perf_counter()
        try:
            with urlopen(req, timeout=5) as response:
                status, body = response.status, json.load(response)
            correct = status == 200 and any(row['id'] == 'sdk-retry' for row in body.get('hits', []))
            error = None
        except HTTPError as response:
            with response:
                status, error, correct = response.code, 'http_error', False
        except (OSError, ValueError) as exc:
            status, error, correct = 0, type(exc).__name__, False
        return {'request_id':request_id, 'status':status, 'correct':correct, 'error':error,
                'latency_ms':(perf_counter()-start)*1000}

    try:
        warmup = one('warmup')
        if not warmup['correct']:
            raise RuntimeError('warmup failed')
        start = perf_counter()
        with ThreadPoolExecutor(max_workers=workers) as pool:
            rows = list(pool.map(one, range(requests)))
        wall = perf_counter() - start
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
    durations = [row['latency_ms'] for row in rows]
    return {'measurement_origin':'local_cpu_measured',
            'scope':'localhost HTTP + lexical retrieval; closed-loop fixed client concurrency; no model or GPU',
            'python':platform.python_version(), 'requests':requests, 'workers':workers,
            'warmup_requests_excluded':1, 'wall_seconds':wall,
            'requests_per_second':requests/wall, 'correct_responses':sum(row['correct'] for row in rows),
            'errors':sum(row['status'] != 200 for row in rows),
            'latency_all_responses_ms':{'mean':statistics.mean(durations),
                'p50':quantile(durations,0.5),'p95':quantile(durations,0.95),'p99':quantile(durations,0.99)},
            'raw_requests':rows}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--requests', type=int, default=40)
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--output', type=Path, default=Path('outputs/p04-benchmark.json'))
    args = parser.parse_args()
    result = benchmark(args.requests, args.workers)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key:value for key,value in result.items() if key != 'raw_requests'}))
