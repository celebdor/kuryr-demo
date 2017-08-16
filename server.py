#!/usr/bin/env python

try:
    from http.server import BaseHTTPRequestHandler
    from http.server import HTTPServer
except ImportError:
    from BaseHTTPServer import BaseHTTPRequestHandler
    from BaseHTTPServer import HTTPServer

import platform
import socket


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        response = '%s: HELLO, I AM ALIVE!!!\n' % platform.node()
        self.wfile.write(response.encode('utf-8'))


class HTTPServerv6(HTTPServer):
    address_family = socket.AF_INET6


if __name__ == '__main__':
    httpd = HTTPServerv6(('::', 8080), Handler)
    httpd.serve_forever()
