# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


dr=webdriver.Chrome() #实例化一个谷歌浏览器对象

dr.get("https://www.baidu.com")

dr.find_element_by_id("kw").send_keys(u"胡歌")
dr.find_element_by_id("su").click()

dr.find_element_by_xpath(".//*[@id='1']/h3/a").click()