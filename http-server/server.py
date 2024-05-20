#!/usr/bin/env python

# -*- coding: UTF-8 -*-


'''
@File          : server.py
@Author        : baojing.he
@Date          : 5/20/2024 4:10 PM
@Description   : 
'''

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging, json


class StatusHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/status':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            json_data = json.loads(post_data)
            print(f"Received JSON data: {json.dumps(json_data, indent=4)}")

        else:
            self.send_error(404, "Not Found")


logging.basicConfig(level=logging.INFO)

with HTTPServer(('', 9000), StatusHandler) as server:
    print("Server started on port 9000")
    server.serve_forever()