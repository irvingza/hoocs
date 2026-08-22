import os
import sys
import http.server
import socketserver

# chdir to an absolute path first: the launch environment's cwd is
# inaccessible, so anything that calls getcwd() before this fails.
site_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
os.chdir(site_dir)

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8377


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Serving {site_dir} on http://127.0.0.1:{PORT}", flush=True)
    httpd.serve_forever()
