# _*_ coding:utf-8 _*_
from selenium import webdriver

'''
浏览器控制器
'''
class Browser_Controller:
    def __init__(self, driver):
        self.driver = driver

    def driver_browser(self, browser_type, base_url):
        if browser_type.lower() == 'firefox':
            driver = webdriver.Firefox()
        elif browser_type.lower() == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Ie()

        driver.get(base_url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def back(self):
        '''
        浏览器后退按钮
        '''
        self.driver.back()

    def forward(self):
        '''
        浏览器前进按钮
        '''
        self.driver.forward()

    def open_url(self, url):
        '''
        打开url站点
        '''
        self.driver.get(url)

    def quit_browser(self):
        '''
        关闭并停止浏览器
        '''
        self.driver.quit()

    def set_browser_window(self, weight, high):
        '''
        设置浏览器窗口
        @param weight:
        @param high:
        '''
        self.driver.set_window_size(weight, high)
