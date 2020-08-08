from page.page_base import Page
from selenium.webdriver.common.by import By
class Checkstand(Page):
    pay_way_loc = (By.XPATH,'//*[@text="微信支付"]')
    pay_affirm_loc = (By.XPATH,'//*[@text="确认支付"]')

    def pay_way(self):
        self.wait_activity('.module.cashierdesk.ui.CashierDeskActivity')
        self.find_element(self.pay_way_loc).click()
        #选择支付方式

    def pay_affirm(self):
        self.find_element(self.pay_affirm_loc).click()
        # 进入支付页
