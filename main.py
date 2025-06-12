import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from generate_title import generate_titles
from hashtags import generate_hashtags


class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, content_type="application/json"):
        self.send_response(200)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/':
            try:
                with open('web_ui.html', 'rb') as f:
                    content = f.read()
                self._set_headers('text/html')
                self.wfile.write(content)
            except FileNotFoundError:
                self.send_error(404, 'web_ui.html not found')
            return

        if parsed.path == '/generate':
            qs = parse_qs(parsed.query)
            topic = qs.get('topic', [''])[0]
            style = qs.get('style', [''])[0]
            titles = generate_titles(topic, style)
            hashtags = generate_hashtags(topic)
            self._set_headers('application/json')
            self.wfile.write(json.dumps({'titles': titles, 'hashtags': hashtags}).encode('utf-8'))
        else:
            self.send_error(404)


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
