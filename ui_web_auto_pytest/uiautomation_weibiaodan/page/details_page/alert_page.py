from page.page_base import Page
from selenium.webdriver.common.by import By
class Alert(Page):
    def order_alert(self):
        self.switch_to_alert()

