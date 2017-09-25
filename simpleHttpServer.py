from http.server import HTTPServer, SimpleHTTPRequestHandler

server = HTTPServer(('',8888), SimpleHTTPRequestHandler)
server.serve_forever();
