from page.page_base import Page
from selenium.webdriver.common.by import By

class OrderHandle(Page):
    ship_loc = (By.NAME,'ship')
    confirmed_delivery_loc = (By.NAME,'delivery_confirmed')
    to_delivery_loc = (By.NAME,'to_delivery')

    def ship_button(self):
        self.find_element(self.ship_loc).click()
        #点击生成发货单
        self.find_element(self.confirmed_delivery_loc).click()
        # 点击确认生成发货单
        # self.wait(self.to_delivery_loc)
        self.find_element(self.to_delivery_loc).click()
        #点击去发货


