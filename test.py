import multiprocessing
import subprocess
import threading
from logging import info
from queue import Queue
from Selenium_Driver import Driver
import psutil



# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
from comunication_client import send_msg
from comunication_server import get_msg


def run_service():

    info("run_service")

    print('service is beginning')
    selenium_server = subprocess.Popen(['java', '-jar', 'selenium-server-standalone-3.0.0-beta4.jar'],
        shell=True,
        universal_newlines=True
    )
    print('service obj returned')

    return selenium_server




def hello(Server_event):
    Server_event.wait(10)
    if Server_event.is_set():
        with Driver() as driver:
            q = Queue()
            server = threading.Thread(target=get_msg, args=([q]))
            server.start()
            print("hello")

            session = driver.get_session()

            driver2 = Driver(session)
            driver.search_google("session1")

            # client = threading.Thread(target=send_msg)
            # client.start()
            # client.join()
            # server.join()
            while True:
                msg = q.get()
                print("get from queue" + str(msg))
                msg = str(msg)
                driver2.search_google(msg)
            print(driver)
            Server_event.clear()
        print("hello done")
    return True




def kill_proc_tree(pid, including_parent=False):
    parent = psutil.Process(pid)
    for child in parent.children(recursive=True):
        child.kill()
    if including_parent:
        parent.kill()

def f(x):
    print(multiprocessing.active_children())
    return x * x
# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes.

# if __name__ == '__main__':
    # selenium_server = run_service()
    # print(selenium_server)
    # hello()

