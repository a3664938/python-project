from page.page_base import Page
from selenium.webdriver.common.by import By
class UserPage(Page):
    login_button_loc = (By.XPATH,'//*[@text="点击登录/注册"]')
    non_payment_loc = (By.XPATH,
                       '//android.widget.LinearLayout[@resource-id=\"cn.tfb.msshop:id/wait_pay\"]/android.view.View[1]/android.view.View[1]')
    set_loc = (By.ID,'cn.tfb.msshop:id/iv_setting_title')
    login_success_loc = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.tfb.msshop:id/tv_phone\"]')

    def login_button(self):
        self.wait(self.login_button_loc)
        self.find_element(self.login_button_loc).click()
        #点击登录按钮，跳转登录页面

    def login_success(self):
        return self.find_element(self.login_success_loc).text

    def main_page_button(self):
        self.wait_activity('.ui.main.MainActivity')
        self.tap_click(57,1218)
        # 进入首页



    def non_payment(self):
        self.wait(self.non_payment_loc)
        self.find_element(self.non_payment_loc).click()

    def set(self):
        self.wait(self.set_loc)
        self.find_element(self.set_loc).click()


