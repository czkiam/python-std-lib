from http.server import HTTPServer, BaseHTTPRequestHandler

class DemoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'this is a GET request')

server = HTTPServer(('',8888), DemoHandler)
server.serve_forever()
