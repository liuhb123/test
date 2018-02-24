# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import canshu

'''
#单个变量参数化及for循环取值
aa={'admin','admin1'}
for user in aa:#定义变量名为user，并从aa列表中循环取值
    url=webdriver.Chrome()
    url.get("http://192.168.20.249:8080/JavaPrj_5/index.do")
    url.find_element_by_id("username").send_keys(user) #引用参数user的值
    time.sleep(1)
    url.find_element_by_id("password").send_keys("admin")
    time.sleep(1)
    url.find_element_by_class_name("right-button01").click()
    time.sleep(1)
    url.quit()
'''

"""
bb={'admin':'admin','admin1':'admin1','admin2':'admin2'}

for user,pwd in bb.items():#定义变量名为user，pwd 并从bb列表中循环取值
    url=webdriver.Chrome()
    url.get("http://192.168.20.249:8080/JavaPrj_5/index.do")
    url.find_element_by_id("username").send_keys(user) #引用参数user的值
    time.sleep(1)
    url.find_element_by_id("password").send_keys(pwd) #引用参数pwd的值
    time.sleep(1)
    url.find_element_by_class_name("right-button01").click()
    time.sleep(1)
    url.quit()

"""

for user,pwd in canshu.para.items():#定义变量名为user，pwd 并从外部参数文件中定义的para列表中循环取值
    url=webdriver.Chrome()
    url.get("http://192.168.20.249:8080/JavaPrj_5/index.do")
    url.find_element_by_id("username").send_keys(user) #引用参数user的值
    time.sleep(1)
    url.find_element_by_id("password").send_keys(pwd) #引用参数pwd的值
    time.sleep(1)
    url.find_element_by_class_name("right-button01").click()
    time.sleep(1)
    url.quit()











