from page.page_base import Page
from selenium.webdriver.common.by import By


class DeliveryList(Page):
    serch_num_loc = (By.NAME,'order_sn')
    backstage_serch_button_loc = (By.CSS_SELECTOR, '[value=" 搜索 "]')
    order_look_loc = (By.LINK_TEXT, '查看')
    delivery_confirmed_loc = (By.NAME,'delivery_confirmed')


    def order_serch(self,order):
        self.find_element(self.serch_num_loc).send_keys(order)
        #输入order
        self.wait(self.backstage_serch_button_loc)

        self.find_element(self.backstage_serch_button_loc).click()
        #点击搜索

    def order_look(self):
        self.wait(self.order_look_loc,timeout=15)
        self.find_element(self.order_look_loc).click()
        # 点击订单查看

    def delivery_confirmed(self):
        self.wait(self.delivery_confirmed_loc,timeout=15)
        self.find_element(self.delivery_confirmed_loc).click()



