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

        self.__wait_start()

        self.stdout.close()


    def __enter__(self):
        # self.prop.start()
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.prop.terminate()
        # self.prop.join()
        self.close()
        print(exc_type)
        # return isinstance(exc_val, exc_type)

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

    def __wait_start(self):
        """
        wait for selenium server set up

        :return: True when selenium server is up False if not
        """
        stout = self.stdout
        server_word = "Selenium Server is up and running"
        used_word = "java.net.BindException: Address already in use: bind"
        while True:
            line = stout.readline()
            print(line)
            if server_word in line:
                print(line)
                # stout.close()
                return True
            elif used_word in line:
                print(line)
                # stout.close()
                return False

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



    server = SelServer()
    robot = threading.Thread(target=hello)
    try:

        # hello()
        print("begin")
        robot.start()
    finally:

        robot.join()

        server.close()


    print("done")