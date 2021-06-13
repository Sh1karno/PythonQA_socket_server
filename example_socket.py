#! /usr/bin/env python3

import socket

from config import ADDRESS, QUEUE
from parser import Parser

with socket.socket() as sock:
    sock.bind(ADDRESS)
    print("Started socket on", ADDRESS)
    sock.listen(QUEUE)
    conn, addr = sock.accept()

    data = conn.recv(4096).decode('utf-8')
    conn.sendall(Parser(data).get_response())
