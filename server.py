#!/usr/bin/env python

import BaseHTTPServer as http
import platform


class Handler(http.BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.end_headers()
    self.wfile.write("%s: HELLO, I AM ALIVE!!!\n" % platform.node())

if __name__ == '__main__':
  httpd = http.HTTPServer(('',80),Handler)
  httpd.serve_forever()
