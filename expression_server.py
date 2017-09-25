from http.server import HTTPServer, BaseHTTPRequestHandler
from collections import OrderedDict
import time
import json

expressions = OrderedDict()


class ExpressionHandler(BaseHTTPRequestHandler):
    def next_id(self):
        if len(expressions) == 0: return 1

        expression_ids = list(expressions.keys())
        last_key = expression_ids[-1]
        return last_key + 1

    def handle_expression(self, x):
        mathop = x['mathop']
        if mathop == 'add':
            return x['op1'] + x['op2']
        elif mathop == 'subtract':
            return x['op1'] - x['op2']
        elif mathop == 'multiply':
            return x['op1'] * x['op2']
        else:
            return None

    def do_GET(self):
        path_parts = self.path.split('/')
        if path_parts[1] == 'list':
            expression_ids = list(expressions.keys())
            expression_list = [
                {
                    'id': expression_id,
                    'mathop': expressions[expression_id]['mathop'],
                    'op1': expressions[expression_id]['op1'],
                    'op2': expressions[expression_id]['op2'],
                    'timestamp': expressions[expression_id]['timestamp']
                }
                for expression_id in expression_ids
            ]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(expression_list).encode('utf-8'))
        elif len(path_parts) > 2 and path_parts[1] == 'expression':
            expression_id = int(path_parts[2])
            if expression_id in expressions.keys():
                expression = expressions[expression_id]
                result = self.handle_expression(expression)
                data = {}
                if result is None:
                    data['error': 'invalid expression']
                else:
                    data['result'] = result
                    data['timestamp'] = time.strftime("%B %d, %Y  %H:%M:%S")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps(data).encode('utf-8'))
            else:
                self.send_response_only(404)
                self.end_headers()
        else:
            self.send_response_only(404)
            self.end_headers()

    def do_POST(self):
        if self.headers['Content-Type'] == 'application/json':
            content_length = int(self.headers['Content-Length'])
            payload = self.rfile.read(content_length)

            timestamp = time.strftime("%B %d, %Y  %H:%M:%S")
            expression_id = self.next_id()

            expression = json.loads(payload.decode('utf-8'))
            expression['timestamp'] = timestamp

            expressions[expression_id] = expression

            self.send_response(201)
            self.end_headers()
            self.wfile.write(json.dumps({'id': expression_id, 'timestamp': timestamp}).encode('utf-8'))
        else:
            self.send_response_only(400)
            self.end_headers()

    def do_PUT(self):
        path_parts = self.path.split('/')
        if len(path_parts) > 1 and self.headers['Content-Type'] == 'application/json':
            expression_id = int(path_parts[1])
            if expression_id in expressions.keys():
                content_length = int(self.headers['Content-Length'])
                payload = self.rfile.read(content_length)
                timestamp = time.strftime("%B %d, %Y  %H:%M:%S")

                expression = json.loads(payload.decode('utf-8'))
                expression['timestamp'] = timestamp

                expressions[expression_id] = expression

                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps({'id': expression_id, 'timestamp': timestamp}).encode('utf-8'))
            else:
                self.send_response_only(404)
                self.end_headers()
        else:
            self.send_response_only(400)
            self.end_headers()


    def do_DELETE(self):
        path_parts = self.path.split('/')
        if len(path_parts) > 1:
            expression_id = int(path_parts[1])
            if expression_id in expressions.keys():
                del expressions[expression_id]
                self.send_response_only(204)
                self.end_headers()
            else:
                self.send_response_only(404)
                self.end_headers()
        else:
            self.send_response_only(404)
            self.end_headers()


if __name__ == '__main__':
    server = HTTPServer(('', 8888), ExpressionHandler)
    server.serve_forever()
