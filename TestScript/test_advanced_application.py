# _*_ coding:utf-8 _*_
from selenium import webdriver
from Util.Mouse_Simulation import Simulate_Mouse
from Util.Keyboard_Simulation import Simulate_Keyboard
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

    def test_simulate_keyboard(self):
        '''
        win32封装键盘方法
        http://www.yfvb.com/help/win32sdk/index.htm?page=html/4luzha.htm
        @return:
        '''
        Simulate_Keyboard.click_onekey('enter')
        Simulate_Keyboard.click_twokey('ctrl', 'v')
        Simulate_Keyboard.click_onekey('enter')
