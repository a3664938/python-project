from page.page_base import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):

    username_input_loc = (By.ID,'u')
    password_input_loc =  (By.ID,'p')
    submit_button_loc = (By.ID,'btnLogin')
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



