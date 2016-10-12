import logging
import multiprocessing
import signal
from logging import info
from multiprocessing import Process
from multiprocessing.pool import Pool

import time

import sys

import psutil
from multiprocessing import Queue

from multiprocessing import Array

from multiprocessing import Pipe
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import randint, random
import os

import subprocess


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def run_service():
    #get process's pid
    # pid = os.getpid()
    # if conn:
    #     conn.send(str(pid))
    #     conn.close()

    info("run_service")

    print('service is beginning')
    selenium_server = subprocess.Popen(['java', '-jar', 'selenium-server-standalone-3.0.0-beta4.jar'])
    # time.sleep(3)
    # selenium_server.send_signal(signal.CTRL_C_EVENT)
    # time.sleep(10)
    # selenium_server.kill()
    print('service obj returned')

    return selenium_server
    # return selenium_server


class Driver:
    # using a driver
    def __init__(self):
        # This is the only code you need to edit in your existing scripts.
        # The command_executor tells the test to run on Sauce, while the desired_capabilities
        # parameter tells us which browsers and OS to spin up.
        _driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
        _driver.implicitly_wait(10)

        self.driver = _driver
        self.session = _driver.session_id

    def switch_driver_session(self, new_session):
        _driver = self.driver
        _driver.quit()
        _driver.session_id = new_session
        self.session = _driver.session_id


    def search_google(self, word):
        # This is your test logic. You can add multiple tests here.
        _driver = self.driver
        _driver.get("http://www.baidu.com")
        if "百度一下" not in _driver.title:
            raise Exception("Unable to load baidu page!")
        elem = _driver.find_element_by_name("wd")
        elem.send_keys(word)
        elem.submit()
        print(_driver.title)
        try:
            links = _driver.find_elements_by_css_selector(".c-abstract")
            [print(link.text) for link in links if link.text]
        finally:
            return links if links else False


def hello():
    print("hello")
    driver = Driver()
    driver2 = Driver()
    # driver3 = Driver()

    session = driver.driver.session_id
    session2 = driver2.driver.session_id

    driver2.switch_driver_session(session)

    driver.search_google("session1")
    driver2.search_google("session2")

    driver.driver.quit()

    print(driver)




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

if __name__ == '__main__':
    # selenium_server = run_service()
    # print(selenium_server)
    try:
        info("Parent")
        pid = os.getpid()
        #创建程序池
        # logging.basicConfig(filename='example.log', level=logging.DEBUG)
        parent_conn, child_conn = Pipe()
        p = Process(target=run_service, args=(child_conn,))
        p.start()
        p2 = Process(target=hello, args=())
        p2.start()

        time.sleep(3)

        print("child pid"+parent_conn.recv())   # prints "[42, None, 'hello']"
    finally:
        p.join()

    try:
        print(multiprocessing.active_children())
        info("p")


        print("starting the process 1")
        # q = Queue()

        # n = Array('i', range(10))

        # pro1 = p.apply_async(run_service)

        print(pro1)

        # print("getting q")
        # print(q.get())
        #等待服务器创建
        # pro1.wait(timeout=5)
        time.sleep(3)
        print("starting the process 2")
        pro2 = p.apply_async(hello)
    finally:
        print('Waiting for all subprocesses done...')
        print(d)
        # p.terminate()
        kill_proc_tree(pid)
        print(multiprocessing.active_children())

        p.terminate()
        p.close()
        p.join()
        print('All subprocesses done.')
        #
        #
        # os.system("dir -l")
    with Pool(4) as p:
        pass


