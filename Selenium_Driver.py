from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Driver:
    # using a driver
    def __init__(self, session=None):
        # This is the only code you need to edit in your existing scripts.
        # The command_executor tells the test to run on Sauce, while the desired_capabilities
        # parameter tells us which browsers and OS to spin up.

        _driver = self.start_driver()
        self.driver = _driver
        self.session = _driver.session_id
        self.session_list = []

        self.add_session(self.session)
        if session:
            self.switch_driver_session(session)
    def start_driver(self):
        print("Driver begin")
        _driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
        _driver.implicitly_wait(10)
        print("Driver etablish")
        return _driver

    def add_session(self, session):
        if not session in self.session_list:
            self.session_list.append(session)

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

    # @staticmethod
    def _reborn_decorator(func):
        def reborn(self, word):
            while True:
                try:
                    func(self, word)
                    return
                except:
                    self.close()
                    self.driver = self.start_driver()

        return reborn
    def login(self, username):
        _driver = self.driver
        # elem = _driver.find_element_by_name("wd")
        _driver.get("https://4acasp.gmcc.net/")
        if "4A" not in _driver.title:
            raise Exception("Unable to load 4A page!")
        login_id = "smsNameText"

        # 输入用户名等待跳转
        login_name = _driver.find_element_by_id(login_id)
        login_button = _driver.find_element_by_css_selector("input.button")

        login_name.send_keys(username)
        # double click
        login_button.click()
        login_button.click()

        # 输入静态密码
        login_psw = _driver.find_element_by_name("smsPwd")
        login_psw.send_keys("mima")

        # 发送验证短信
        send_phone = _driver.find_element_by_id("sendsms_btn")
        send_phone.click()
        send_phone.click()

    def input_dynamic(self, sms_pwd):
        _driver = self.driver
        dynamic_smsPwd = _driver.find_element_by_name("dynamic_smsPwd")
        dynamic_smsPwd.send_keys(sms_pwd)

        login_assure = _driver.find_element_by_id("sb_btn")
        login_assure.click()
        a=1
        a=2




    @_reborn_decorator
    def search_google(self, word):
        # This is your test logic. You can add multiple tests here.

        _driver = self.driver
        # _driver.get("http://www.baidu.com")
        # _driver.get("https://4acasp.gmcc.net/")
        # if "4A" not in _driver.title:
        #     raise Exception("Unable to load 4A page!")

        # elem = _driver.find_element_by_name("wd")
        # elem.send_keys(word)
        # elem.submit()

        print(_driver.title)
        # all_cookies = _driver.get_cookies()
        # print(all_cookies)

        # links = False
        # try:
        #     links = _driver.find_elements_by_css_selector(".c-abstract")
        #     [print(link.text) for link in links if link.text]
        # finally:
        #     return links if links else False

