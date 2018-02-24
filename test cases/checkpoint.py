# coding:utf-8
from selenium import webdriver
import time

url= webdriver.Chrome()
url.get("http://192.168.20.249:8080/JavaPrj_5/index.do")
url.find_element_by_id("username").send_keys("admin")
time.sleep(1)
url.find_element_by_id("password").send_keys("admin")
time.sleep(1)
url.find_element_by_class_name("right-button01").click()
time.sleep(1)

url.switch_to.parent_frame()
url.switch_to.frame("leftFrame")

try:
        #url.find_element_by_xpath("html/body/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[1]/td[1]/img")
        url.find_element_by_xpath("html/body/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[1]/td[2]/span")
        print ("登录成功1")
except Exception as e:
        url.get_screenshot_as_file("D:\\pythonpic\\error.png")  # 错误截图保存在指定位置
        print ("登录失败")
