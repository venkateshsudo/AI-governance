"""Local static server for the Aegis AI governance MVP.

Usage:
    python serve.py            # serves on the first free port from 8000
    python serve.py 8080       # serves on a specific port

No third-party dependencies are required.
"""

from __future__ import annotations

import http.server
import os
import socket
import socketserver
import sys
import threading
import webbrowser
from functools import partial

ROOT = os.path.dirname(os.path.abspath(__file__))


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt: str, *args: object) -> None:  # noqa: D401
        sys.stdout.write("  %s\n" % (fmt % args))


def find_port(preferred: int) -> int:
    for port in range(preferred, preferred + 20):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise SystemExit("Could not find a free port between %d and %d." % (preferred, preferred + 19))


def main() -> None:
    preferred = 8000
    if len(sys.argv) > 1:
        try:
            preferred = int(sys.argv[1])
        except ValueError:
            raise SystemExit("Port must be a number, for example: python serve.py 8000")

    port = find_port(preferred)
    handler = partial(QuietHandler, directory=ROOT)
    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    url = f"http://localhost:{port}/"

    print()
    print("  Aegis · AI governance workspace")
    print(f"  Serving {ROOT}")
    print(f"  Open {url}")
    print("  Press Ctrl+C to stop")
    print()

    threading.Timer(0.7, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
