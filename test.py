import multiprocessing
import os
import subprocess
from logging import info

import psutil
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def run_service():

    info("run_service")

    print('service is beginning')
    selenium_server = subprocess.Popen(['java', '-jar', 'selenium-server-standalone-3.0.0-beta4.jar'],
        shell=True,
        universal_newlines=True
    )
    print('service obj returned')

    return selenium_server


class Driver:
    # using a driver
    def __init__(self, session=None):
        # This is the only code you need to edit in your existing scripts.
        # The command_executor tells the test to run on Sauce, while the desired_capabilities
        # parameter tells us which browsers and OS to spin up.
        _driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
        _driver.implicitly_wait(10)

        self.driver = _driver
        self.session = _driver.session_id
        if session:
            self.switch_driver_session(session)

    def switch_to_frame(self, frame_name):
        driver = self.driver
        driver.switch_to.frame(frame_name)

    def switch_to_active_element(self):

        """
        for  finding out element
        """
        self.driver.switch_to.active_element()

    def switch_to_default_content(self):
        self.driver.switch.to_default_content()

    def get_current_handle(self):
        return self.driver.current_window_handle

    def get_handles(self):
        return self.driver.window_handles

    def switch_driver_session(self, new_session):
        _driver = self.driver
        _driver.quit()
        _driver.session_id = new_session
        self.session = _driver.session_id

    def switch_to_handle(self, handle):
        _driver = self.driver
        _driver.switch_to.window(handle)

    def get_session(self):
        return self.session

    def close(self):
        self.driver.quit()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
        print(exc_val)

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
        all_cookies = _driver.get_cookies()
        print(all_cookies)
        links = False
        try:
            links = _driver.find_elements_by_css_selector(".c-abstract")
            [print(link.text) for link in links if link.text]
        finally:
            return links if links else False


def hello():
    try:
        print("hello")
        driver = Driver()
        # driver3 = Driver()

        session = driver.driver.session_id

        driver2 = Driver(session)

        driver.search_google("session1")
        driver2.search_google("session2")
    finally:

        driver.close()
        # driver3.close()

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
    pass

