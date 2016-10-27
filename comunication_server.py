# Echo server program
import json
import socket

from json import JSONDecodeError
from queue import Queue


class socketServer():
    def __init__(self, q):
        self.address = ("", 6101)
        # make an socket instance
        self.socket = socket.socket()
        # start as a server
        self.start_server()
        # receive one msg and print and send
        while True:
            try:

                self.print_msg(q)
                print("连接结束")
                # break
                # break
            except:
                print("出现故障")


    def start_server(self):
        print("socket server start")
        self.socket.bind(self.address)
        self.socket.listen(1)


    def print_msg(self, q):
        print("listen")
        conn, addr = self.socket.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                d = data.decode('utf-8')

                if d:
                    try:
                        d = json.loads(d)
                    except JSONDecodeError as e:
                        pass
                    print(type(d))
                    print(d)
                    if q.empty():
                        q.put(d)
                        break
                    print("-------------------------")
                # print(type(data))
                # print(d['test'])
                if not data:
                    break
                conn.sendall(data)
                # break
    def close(self):
        self.socket.close()

def get_msg(q):
    sever = socketServer(q)

if __name__ == '__main__':
    # sever = socketServer()
    # sever.close()
    q = Queue()
    q.put("nice")
    sever = socketServer(q)
    # text = str(q.get())

    pass