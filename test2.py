import time

from test import *
import threading


class SelServer:

    def __init__(self):
        """
        start a selenium server and wait for it
        """
        cmd = self.__get_start_cmd()
        self.pro = self.__execute_cmd(cmd)
        self.stdout = self.pro.stdout
        # self.__wait_start()
        # self.stdout.close()


    def __enter__(self):
        return self
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        print(exc_type)

    def __get_start_cmd(self):
        cmd = ['java', '-jar', 'selenium-server-standalone-3.0.0-beta4.jar']
        return cmd

    @staticmethod
    def __execute_cmd(cmd) -> subprocess.Popen:
        """
        take in a cmd and exicute it in with subprocess.Popen and create a pip line

        :return: Popen instance
        """
        pro = subprocess.Popen(cmd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               universal_newlines=True)
        return pro

    def server_printer(self, server_event):
        """
        wait for selenium server set up realeasing event
        :return: True when selenium server is up False if not
        """
        stout = self.stdout
        # stout.close()
        server_word = "Selenium Server is up and running"
        used_word = "java.net.BindException: Address already in use: bind"
        signal = False
        counter = 0
        while True:
            # wait for a line of the subprocess
            line = stout.readline()
            # print(line)
            if server_word in line:
                print(line)
                # set server_event
                server_event.set()
                signal = True
            elif used_word in line:
                print(line)
                stout.close()
                return False
            counter += 1
            # print(counter)
            if signal:
                # print(server_event.is_set())
                # server_event have to be unset before realine could not stout.read anything
                if not server_event.is_set():
                    stout.close()
                    print("server_std exiting")
                    return True

    def __print(self, stdout):
        try:
            while True:
                line = stdout.readline()
                print(line)
        finally:
            stdout.close()

    def close(self):
        # self.pro.terminate()
        self.pro.kill()

# def start_server():
#     SelServer

if __name__ == '__main__':
    print("装配线程")
    info("this is main")



    with SelServer() as server:


        server_event = threading.Event()
        server_std = threading.Thread(target=server.server_printer, args=([server_event]))
        robot = threading.Thread(target=hello, args=([server_event]))

        try:

            # hello()
            print("Thread is beginning")
            server_std.start()
            robot.start()

        finally:
            robot.join()
            server_std.join()

    # print("here")

    # print(server_std.is_alive())
