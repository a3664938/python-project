from page.page_base import Page
# from testcase.test_base import TestBase
from selenium.webdriver.common.by import By

class OrderSuccess(Page):
    order_number_loc = (By.CSS_SELECTOR,'[style="color:red"]')

    def order_number(self):
        return self.find_element(self.order_number_loc).text
        #获取订单号