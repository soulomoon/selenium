# Echo client program
import json
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(socket.gethostname())
    # s.send_byte("1")
    a = {'test': "太阳出来聊liao", 'dict': {1: 2, 3: 4}, 'list': [42, 16]}
    b = json.dumps(a).encode('utf-8')
    s.sendall(b)
    print("sneded")
    data = s.recv(1024)
print('Received', repr(json.loads(data.decode('utf-8'))))