# _*_ coding:utf-8 _*_
from selenium import webdriver
from Util.Mouse_Simulation import Simulate_Mouse
from Util import BrowserController
import unittest
import time

class Test_Advanced_Application(unittest.TestCase):
    def setUp(self):
        self.url = 'http://www.baidu.com'


    def test_simulate_mouse(self):
        '''
        调用模拟鼠标方法
        @return:
        '''
        chr_driver = webdriver.Chrome()
        chr_driver.maximize_window()
        chr_driver.get(self.url)
        element = chr_driver.find_element_by_id('s-usersetting-top')
        Simulate_Mouse(chr_driver).right_click(element)
        time.sleep(5)