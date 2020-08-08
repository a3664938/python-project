from page.page_base import Page
from selenium.webdriver.common.by import By
class Goods(Page):


    def buy_button(self):
        self.wait_activity('.module.productdetail.ui.ProductDetailActivity')
        self.tap_click(514,1222)
        # 点击购买，进入订单页

    def back(self):
        self.wait_activity('.module.productdetail.ui.ProductDetailActivity')
        self.driver.back()
        #点击返回，返回至促销页