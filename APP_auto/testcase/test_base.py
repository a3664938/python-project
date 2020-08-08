from appium import webdriver
import unittest
class TestBase(unittest.TestCase):
    def setUp(self):
        desired_capabilities = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:62001',
            'platformVersion': '4.4.2',  # 逍遥模拟器
            # 'platformVersion': '7.1.1',    # 小米真机
            'appPackage': 'cn.tfb.msshop',
            'appActivity': 'cn.tfb.msshop.ui.main.MainSplashActivity',
            # 'browserName': 'Browser',
            # "automationName": "selendroid",
            'noReset': 'true',
            # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
            'newCommandTimeout': 600,
            # 设置屏幕方向,LANDSCAPE(横向) or PORTRAIT(纵向)
            # 'orientation':'LANDSCAPE'
            'automationName':'Uiautomator2'
        }


        # self.driver.implicitly_wait(10)

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    def tearDown(self):

        self.driver.quit()

