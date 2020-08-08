from page.page_base import Page
from selenium.webdriver.common.by import By


class BackstageLoginPage(Page):

    username_input_loc = (By.NAME,'username')
    password_input_loc =  (By.NAME,'password')
    submit_button_loc = (By.CSS_SELECTOR,'[value="进入管理中心"]')
    #定位器

    def username_input(self,text):
        self.wait(self.username_input_loc)
        self.find_element(self.username_input_loc).click()
        self.find_element(self.username_input_loc).send_keys(text)

    def password_input(self,text):
        self.find_element(self.password_input_loc).click()
        self.find_element(self.password_input_loc).send_keys(text)

    def submit_button(self):
        self.find_element(self.submit_button_loc).click()
