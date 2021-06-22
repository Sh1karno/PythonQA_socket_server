#! /usr/bin/env python3

import socketserver

from config import ADDRESS
from parser import Parser


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(4096).decode('utf-8')
        self.request.sendall(Parser(data).get_response())


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":

    with ThreadedTCPServer(ADDRESS, ThreadedTCPRequestHandler) as server:
        print("Started socket on", ADDRESS)
        server.serve_forever()
