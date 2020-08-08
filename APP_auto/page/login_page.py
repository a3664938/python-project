from page.page_base import Page
from selenium.webdriver.common.by import By

class Logining(Page):
    username_loc = (By.ID,'cn.tfb.msshop:id/pay_name_edit')
    password_loc = (By.ID,'cn.tfb.msshop:id/check_pwd_edit')
    login_loc = (By.XPATH,'//android.widget.Button[@resource-id=\"cn.tfb.msshop:id/login\"]')

    def username(self,username):
        self.wait_activity('.ui.user.UserLoginActivity')
        self.find_element(self.username_loc).clear()
        self.find_element(self.username_loc).send_keys(username)
        #输入用户名

    def password(self,password):
        self.find_element(self.password_loc).send_keys(password)
        #输入密码

    def login(self):
        self.find_element(self.login_loc).click()

