#-*-coding:utf-8 -*-
#@time:2021/4/211:30
#@author:wxing
#@File:WebDemo.py
#@Software:PyCharm Community Edition
from selenium import webdriver
from time import sleep
def browser(type_):
    try:
        driver = getattr(webdriver,type_)()
    except Exception as e:
        print("出现异常时使用Chrome")
        driver= webdriver.Chrome()
    return driver
class WebDemo:
    driver = None
    def __init__(self,type_):
        self.driver= browser(type_)
    #访问
    def visit(self,**kwargs):
        self.driver.get(kwargs['txt'])
    #定位
    def locator(self,**kwargs):
        return self.driver.find_element(kwargs['name'],kwargs['va'])
    #输入
    def input(self,**kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])
    #点击
    def click(self,**kwargs):
        self.locator(**kwargs).click()
    #等待
    def wait(self,**kwargs):
        sleep(kwargs['txt'])
    #退出
    def quit(self,**kwargs):
        self.driver.quit()
