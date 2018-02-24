#coding=utf-8
from selenium import webdriver  #到webdriver包
import time #到time包
from selenium.webdriver.support.wait import WebDriverWait
#from time import sleep

dr=webdriver.Chrome() #实例化一个谷歌浏览器对象

dr.get("http://127.0.0.1:1080/WebTours/")

dr.switch_to.default_content()
dr.switch_to.frame("body")
dr.switch_to.frame("navbar")
sreach_window2=dr.current_window_handle

print sreach_window2

dr.find_element_by_xpath("html/body/form/table/tbody/tr[4]/td[2]/input").send_keys("liuhb")
dr.find_element_by_xpath("html/body/form/table/tbody/tr[6]/td[2]/input").send_keys("123456")
dr.find_element_by_xpath("html/body/form/table/tbody/tr[9]/td[2]/input").click()
dr.switch_to.default_content()
dr.switch_to.frame("body")
dr.switch_to.frame("navbar")

dr.find_element_by_xpath("html/body/center/center/a[1]/img").click()




