from page.page_base import Page
from selenium.webdriver.common.by import By

class ShoppingCart(Page):

    settlement_button_loc = (By.CSS_SELECTOR,'[alt="checkout"]')

    def settlement_button(self):
        self.find_element(self.settlement_button_loc).click()

