from selenium import webdriver

driver = webdriver.Ie()
driver.implicitly_wait(10) # seconds
# driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
# driver.get('qq.com')
try:
	driver.get('baidu.com')
	search_box = driver.find_element_by_id("kw")
	search_box.send_keys("时间间")
	search_box.send_keys("时间间")
	search_box.send_keys("时间间")
	search_box.send_keys("时间间")
	search_box.send_keys("时间间")
	search_box.send_keys("时间间")
	search_box.send_keys("sfdsfdsfadsf;sadfjakfjas;ldfjsdkjfsak;djfsajfsjf;sghSGHWGNSKDMVSLDLSaDSJ'FSAHG'HASGS间间时间间时间间时间间时间间时间间时间间时间间时间间时间间时间间时间间时间间时间间时间间时间间时间间时间间时间间时间间时间间间间")
	search_box.submit()
except:
	print("error")
finally:
	driver.close()
