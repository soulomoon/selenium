# Echo client program
import json
import socket

import time

HOST = 'localhost'    # The remote host
PORT = 6101              # The same port as used by the server
print(socket.getaddrinfo(HOST, PORT))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(socket.gethostname())
    # s.send_byte("1")
    a = {'test': "太阳出来聊", 'dict': {1: 2, 3: 4}, 'list': [42, 16]}
    b = json.dumps(a).encode('utf-8')
    s.sendall(b"22")
    print("sneded")
    data = s.recv(1024)
    print('Received', data)
    # time.sleep(5)
    send = s.send(b"time")
    print(send)
    data2 = s.recv(1024)
    s.close()

print('Received', data2)