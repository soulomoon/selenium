# Echo client program
import socket


# send = s.send(b"time")
# print(send)
# data2 = s.recv(1024)
def send_msg():
    """
    send to socket server of 6101
    """
    HOST = 'localhost'  # The remote host
    PORT = 6101  # The same port as used by the server
    print(socket.getaddrinfo(HOST, PORT))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(socket.gethostname())
        mstr = "密码".encode()

        # a = {'test': mstr, 'dict': {1: 2, 3: 4}, 'list': [42, 16]}

        # b = json.dumps(a).encode('utf-8')
        s.sendall(mstr)

        print("send")
        data = s.recv(1024)
        print('Received', data)
        s.close()


if __name__ == '__main__':
    send_msg()
    # print('Received', data2)
