"""P04: localhost-only HTTP teaching adapter. Production hosting is a course task."""
from __future__ import annotations

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
import secrets
from threading import BoundedSemaphore

from .retrieval import SearchIndex, load_documents


def make_server(host="127.0.0.1", port=8000, *, credentials: dict[str, str], index=None,
                max_inflight=4):
    if host not in {"127.0.0.1", "localhost"}:
        raise ValueError("teaching server must bind to localhost")
    if not credentials or any(not token or not tenant for token, tenant in credentials.items()):
        raise ValueError("nonempty server-side credentials are required")
    search_index = index if index is not None else SearchIndex(load_documents())
    capacity = BoundedSemaphore(max_inflight)

    class Handler(BaseHTTPRequestHandler):
        def setup(self):
            super().setup()
            self.connection.settimeout(5)

        def log_message(self, *args):
            pass  # Keep auth headers and content out of default teaching logs.

        def reply(self, code, body):
            raw = json.dumps(body).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(raw)))
            self.send_header("Connection", "close")
            self.end_headers()
            self.wfile.write(raw)
            self.close_connection = True

        def do_GET(self):
            if self.path == "/health":
                self.reply(200, {"status": "ok", "scope": "local teaching service"})
            else:
                self.reply(404, {"error": "not_found"})

        def do_POST(self):
            if self.path != "/v1/search":
                self.reply(404, {"error": "not_found"})
                return
            auth = self.headers.get("Authorization", "")
            tenant = next((value for token, value in credentials.items()
                           if secrets.compare_digest(auth.encode("utf-8"), ("Bearer " + token).encode("utf-8"))), None)
            if tenant is None:
                self.reply(401, {"error": "unauthorized"})
                return
            if not capacity.acquire(blocking=False):
                self.reply(429, {"error": "capacity_exceeded"})
                return
            try:
                try:
                    if self.headers.get("Transfer-Encoding"):
                        raise ValueError("transfer encoding unsupported")
                    length = int(self.headers.get("Content-Length", "0"))
                    if length <= 0 or length > 16_384:
                        raise ValueError("invalid request size")
                    body = json.loads(self.rfile.read(length))
                    if not isinstance(body, dict) or set(body) - {"query", "k"}:
                        raise ValueError("unexpected request fields")
                    hits = search_index.search(body.get("query"), tenant, body.get("k", 3))
                except (ValueError, TypeError, UnicodeDecodeError, TimeoutError):
                    self.reply(400, {"error": "invalid_request"})
                    return
                except Exception:
                    self.reply(500, {"error": "internal_error"})
                    return
                self.reply(200, {"hits": hits, "tenant": tenant, "generation_evaluated": False})
            finally:
                capacity.release()

    return ThreadingHTTPServer((host, port), Handler)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    token = os.environ.get("AI_PATH_TOKEN")
    if not token:
        parser.error("set AI_PATH_TOKEN to a local demonstration token")
    server = make_server(port=args.port, credentials={token: "demo"})
    print(f"Local teaching service: http://127.0.0.1:{server.server_port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
