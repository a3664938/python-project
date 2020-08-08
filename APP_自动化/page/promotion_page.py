from page.page_base import Page
from selenium.webdriver.common.by import By
class Promotion(Page):
    back_loc = (By.ID,'cn.tfb.msshop:id/textView_back')


    def go_buy(self):
        self.wait_activity('.module.limitsales.ui.LimitSalesActivity')
        self.tap_click(638, 243)
        # 进入商品页

    def back(self):
        self.wait_activity('.module.limitsales.ui.LimitSalesActivity')
        self.find_element(self.back_loc).click()
        #

