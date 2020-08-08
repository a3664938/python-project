from page.page_base import Page
from selenium.webdriver.common.by import By


class CreatOrder(Page):
    delivery_way_loc = (By.NAME,'shipping')
    payment_way_loc = (By.NAME,'payment')
    pack_way_loc = (By.NAME,'pack')
    card_way_loc = (By.NAME,'card')
    submit_order_loc = (By.CSS_SELECTOR,'[src="themes/ecmoban_meilishuo/images/bnt_subOrder.gif"]')
    count_pay_loc = (By.CSS_SELECTOR,'#ECS_ORDERTOTAL>:nth-child(1)>:nth-child(1)>:nth-child(3)>td')


    def shipping_way(self):
        self.find_elements(self.delivery_way_loc)[1].click()

    def payment_way(self):
        self.find_elements(self.payment_way_loc)[3].click()

    def pack_way(self):
        self.find_elements(self.pack_way_loc)[0].click()

    def card_way(self):
        self.find_elements(self.card_way_loc)[0].click()

    def submit_order(self):
        self.find_element(self.submit_order_loc).click()

    def count_pay(self):
        return self.find_element(self.count_pay_loc).text[8:-1]



