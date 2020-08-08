from page.page_base import Page
from selenium.webdriver.common.by import By

class SetPage(Page):
    logout_loc = (By.XPATH,'//*[@text="退出登录"]')
    logout_affirm_loc = (By.XPATH,'//*[@text="确定"]')
    def logout(self):
        self.wait_activity('.ui.mine.MineSettingActivity')
        self.find_element(self.logout_loc).click()

    def logout_affirm(self):
        self.wait(self.logout_affirm_loc)
        self.find_element(self.logout_affirm_loc).click()