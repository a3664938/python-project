import datetime

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Page():

    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)

    def find_element(self,locator):
        return self.driver.find_element(*locator)

    def find_elements(self,locator):
        return self.driver.find_elements(*locator)

    def switch_to_frame(self,locator):
        self.driver.switch_to_frame(locator)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def select(self,locator,value):
        select_ = self.find_element(locator)
        sel_obj = Select(select_)
        if isinstance(value,int):
            sel_obj.select_by_index(value)
        elif isinstance(value,str):
            sel_obj.select_by_visible_text(value)

    def wait(self,locator,timeout=10):
        wait_ = WebDriverWait(self.driver,timeout)
        wait_.until(lambda driver:driver.find_element(*locator))

    def switch_to_window(self):

        self.driver.switch_to.window(self.driver.window_handles[-1])
        #切换到新开页面

    def switch_to_alert(self):
        self.driver.switch_to.alert.accept()

    def keys_enter(self,locator): # 回车键
        return self.driver.find_element(*locator).send_keys(Keys.ENTER)

    # def exception_monitor(path):
    #     def decorator(func):
    #         def wrapper(self, *args, **kw):
    #             try:
    #                 # 捕获函数异常
    #                 return func(self, *args, **kw)
    #             except Exception:
    #                 s = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')  # 现在
    #                 print (s)
    #                 # 函数出现异常后的处理
    #                 if path.endswith('/'):
    #                     self.driver.save_screenshot(path + func.__name__ + '%s_error.png' % s )
    #                 else:
    #                     self.driver.save_screenshot(path + '/' + func.__name__ + '%s_error.png' % s )
    #                 # 为了能在结果展示异常，需要重新抛出该异常
    #                 raise
    #
    #         return wrapper
    #
    #     return decorator






