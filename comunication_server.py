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
        # try:
        while True:
            try:
                self.print_msg(q)
                print("连接结束")
            except:
                print("one socket down")

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
                    print(d)
                    print("-------------------------")
                    if q.empty():
                        q.put(d)
                        break
                if not data:
                    break
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
