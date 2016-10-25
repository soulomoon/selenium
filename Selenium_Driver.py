from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Driver:
    # using a driver
    def __init__(self, session=None):
        # This is the only code you need to edit in your existing scripts.
        # The command_executor tells the test to run on Sauce, while the desired_capabilities
        # parameter tells us which browsers and OS to spin up.
        print("Driver begin")
        _driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
        _driver.implicitly_wait(10)
        print("Driver etablish")

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
        print("driver quit begin")

        self.driver.quit()
        print("driver quit done")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
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
        # links = False
        # try:
        #     links = _driver.find_elements_by_css_selector(".c-abstract")
        #     [print(link.text) for link in links if link.text]
        # finally:
        #     return links if links else False
