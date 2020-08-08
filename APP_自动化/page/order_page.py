from page.page_base import Page
from selenium.webdriver.common.by import By

class OrderList(Page):

    def submit_order(self):
        self.wait_activity('.module.orders.ui.OrderConfirmActivity')
        self.tap_click(700,1222)
        # 提交订单

