from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

user_name = 'yyzhichengshiceshi7'
web_path = "https://4acasp.gmcc.net///auth/nextlogin.jsp?target=https%3A%2F%2F4a.gmcc.net%2Ffirst.do%3Fmethod%3Dlogin&appCode=IAM000"
driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)

driver.get(web_path)
# 输入登录名
input = driver.find_element_by_id("smsNameText")
input.clear()
input.send_keys(user_name)


driver.quit()