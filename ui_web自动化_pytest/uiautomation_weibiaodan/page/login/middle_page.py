from page.page_base import Page
from selenium.webdriver.common.by import By

class MiddlePage(Page):

    alert_login_success_div_loc = (By.CSS_SELECTOR, '[style="font-size: 14px; font-weight:bold; color: red;"]')
    #定位器


    def alert_login_success(self):

        self.wait(self.alert_login_success_div_loc)
        return self.find_element(self.alert_login_success_div_loc).text
