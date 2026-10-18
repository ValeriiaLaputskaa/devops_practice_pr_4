from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok"}).encode('utf-8'))

HTTPServer(('localhost', 8080), RequestHandler).serve_forever()
