# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import canshu
import canshu_1

chrome = webdriver.Chrome()
chrome.get("http://192.168.20.6:8080/JavaPrj_5/index.do")
time.sleep(2)


'''
chrome.refresh()
chrome.back()
time.sleep(3)
chrome.forward()

chrome.set_window_size(960,540)
time.sleep(1)
chrome.maximize_window()
chrome.get_screenshot_as_file("d:\\pythonpic\\bb.png")
'''
#系统登录
chrome.find_element_by_id("username").send_keys("admin")
time.sleep(1)
chrome.find_element_by_name("password").send_keys("admin")
time.sleep(1)
chrome.find_element_by_class_name("right-button01").send_keys(Keys.ENTER)
time.sleep(2)


    # 添加人员信息
chrome.switch_to.parent_frame()  # 返回父窗口
chrome.switch_to.frame("leftFrame") # 跳转至leftFrame窗口
"""
    # 登录成功添加检查点验证
    try:

        chrome.find_element_by_xpath("html/body/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[1]/td[1]/img")
        print ("登录成功")
    except Exception as e:
        chrome.get_screenshot_as_file("D:\\pythonpic\\error.png")  # 错误截图保存在指定位置
        print ("登录失败")
"""

chrome.find_element_by_xpath("html/body/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td[2]/a").click()
# chrome.find_element_by_xpath("//*[text()='人员管理']").click()
time.sleep(2)

chrome.find_element_by_xpath(".//*[@id='subtree8']/tbody/tr[1]/td[2]/a").click()
# chrome.find_element_by_xpath("//*[text()='人员信息录入']").click()
time.sleep(2)

chrome.switch_to.parent_frame()
chrome.switch_to.frame("mainFrame")

chrome.find_element_by_name("username").send_keys("user1")
chrome.find_element_by_name("password").send_keys("pwd1")
chrome.find_element_by_xpath("html/body/form/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td[2]/input[2]").click()
chrome.find_element_by_id("birthday").send_keys("1989-01-01")
chrome.find_element_by_name("isadminhelp").click()
chrome.find_element_by_name("content").send_keys(u"我是雷锋")
chrome.find_element_by_name("提交").click()

for user in canshu_1.parameters:
#for user,pwd in canshu.para.items():
    chrome.switch_to.parent_frame()
    chrome.switch_to.frame("leftFrame")
    chrome.find_element_by_xpath(".//*[@id='subtree8']/tbody/tr[1]/td[2]/a").click()
    time.sleep(2)
    chrome.switch_to.parent_frame()
    chrome.switch_to.frame("mainFrame")
    chrome.find_element_by_name("username").send_keys(user)
    chrome.find_element_by_name("password").send_keys("、")
    chrome.find_element_by_xpath("html/body/form/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td[2]/input[2]").click()
    chrome.find_element_by_id("birthday").send_keys("1989-01-01")
    chrome.find_element_by_name("isadminhelp").click()
    chrome.find_element_by_name("content").send_keys(u"你们都是好学生")
    chrome.find_element_by_name("提交").click()

'''
#更新用户信息
chrome.find_element_by_xpath(".//*[@id='subtree1']/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td[7]/a[1]").click()
time.sleep(2)
chrome.find_element_by_id("username").send_keys(Keys.BACKSPACE)  # 回退1次
chrome.find_element_by_id("username").send_keys(Keys.BACKSPACE)  # 回退2次
chrome.find_element_by_id("username").send_keys("23")  # 更新信息
chrome.find_element_by_xpath("html/body/form/div/table/tbody/tr[3]/td/input[1]").click() # 提交更新信息
time.sleep(2)

# 删除用户信息
chrome.find_element_by_xpath(".//*[@id='subtree1']/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[6]/td[7]/a[2]").click()
time.sleep(2)

# 查询人才库列表信息
chrome.switch_to.parent_frame()
chrome.switch_to.frame("leftFrame")
chrome.find_element_by_xpath("//*[text()='招聘管理']").click()
time.sleep(2)
chrome.find_element_by_xpath(".//*[@id='subtree7']/tbody/tr[3]/td[2]/a").click()
'''



