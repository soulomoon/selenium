# Echo server program
import json
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 6101              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:

        conn, addr = s.accept()
        # print(addr)
        # print('begin')
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                d = data.decode('utf-8')
                # if data: print(data)
                if 1: print(d)
                # print(type(data))
                # print(d['test'])
                if not data: break
                conn.sendall(data)
                # break

