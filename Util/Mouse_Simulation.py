# _*_ coding:utf-8 _*_
from selenium.webdriver.common.action_chains import ActionChains

class Simulate_Mouse:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    # 按一下鼠标左键
    def left_click(self, element):
        self.actions.click(element).perform()

    # 按两下鼠标左键
    def double_left_click(self, element):
        self.actions.double_click(element).perform()

    # 按一下鼠标右键
    def right_click(self, element):
        self.actions.context_click(element).perform()

    # 移动鼠标到element
    def move_mouse(self, element):
        self.actions.move_to_element(element).perform()

    # 拖拽到某个元素然后松开
    def move_mouse_source_target(self, source, target):
        self.actions.drag_and_drop(source, target)
    # 效果同上 release释放
    def move_source_target(self, source, target):
        self.actions.click_and_hold(source).release(target).perform()

    # 拖拽元素到坐标（x,y)
    def drag_element(self, element, x, y):
        self.actions.click_and_hold(element).move_by_offset(x, y).release().perform()
        # self.actions.drag_and_drop_by_offset(element, x, y)

    # 按住并且不释放
    def click_hold(self, element):
        self.actions.click_and_hold(element)