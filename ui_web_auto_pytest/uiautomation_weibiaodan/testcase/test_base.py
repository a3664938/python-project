from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
import datetime


def exception_monitor(path):
    def decorator(func):
        def wrapper(self, *args, **kw):
            try:
                # 捕获函数异常
                return func(self, *args, **kw)
            except Exception:
                s = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')  # 现在
                print (s)
                # 函数出现异常后的处理
                if path.endswith('/'):
                    self.driver.save_screenshot(path + func.__name__ + '%s_error.png' % s )
                else:
                    self.driver.save_screenshot(path + '/' + func.__name__ + '%s_error.png' % s )
                    print(path + '/' + func.__name__ + '%s_error.png' % s )
                # 为了能在结果展示异常，需要重新抛出该异常
                raise

        return wrapper

    return decorator


class TestBase(unittest.TestCase):


    def setUp(self):
        options = Options()
        options.add_argument('-headless')
        #self.driver = webdriver.Chrome(options=options)   # 无头模式
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()

    def tearDown(self):

        self.driver.quit()


