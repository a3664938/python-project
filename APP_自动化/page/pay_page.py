from page.page_base import Page
from selenium.webdriver.common.by import By
class Pay(Page):
    pay_cancel_loc = (By.ID,'com.tencent.mm:id/ht')
    pay_cancel_affirm_loc = (By.XPATH,'//*[@text="确认"]')
    back_loc = (By.ID,'cn.tfb.msshop:id/iv_back')

    def pay_cancel(self):
        self.wait_activity('.plugin.wallet.pay.ui.WalletPayUI')
        self.find_element(self.pay_cancel_loc).click()
        # 点击返回，弹出弹框

    def pay_cancel_affirm(self):
        self.wait_activity('.wxapi.WXPayEntryActivity')
        self.find_element(self.pay_cancel_affirm_loc).click()
        # 确认取消支付
    def back(self):
        self.wait_activity('.module.cashierdesk.ui.CashierDeskActivity')
        self.find_element(self.back_loc).click()
        # 返回至商品页
