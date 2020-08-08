from selenium.webdriver.support.wait import WebDriverWait
class Page():

    def __init__(self,driver):
        self.driver = driver

    def find_element(self,locator):
        return self.driver.find_element(*locator)

    def wait(self,locator,timeout=10):
        wait_ = WebDriverWait(self.driver,timeout)
        wait_.until(lambda driver:driver.find_element(*locator))

    def tap_click(self,a, b):
        self.driver.tap([(a, b)], 500)

    def wait_activity(self,activity):
        self.driver.wait_activity(activity,10)

    # def current_activity(self):
    #         return self.driver.current_activity