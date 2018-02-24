# coding:utf-8
from selenium import webdriver
aaa=webdriver.Chrome()
aaa.get("https://www.baidu.com")
#aaa.find_elements_by_class_name("mnav")[2].click()

aaa.find_element_by_id("kw").send_keys(u"软件测试")
print("a")
a="123"
print(a)







