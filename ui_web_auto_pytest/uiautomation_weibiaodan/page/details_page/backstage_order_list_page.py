from page.page_base import Page
from selenium.webdriver.common.by import By
from page.details_page.order_success_bage import OrderSuccess
# from testcase.test_base import TestBase
from time import sleep


class OrderList(Page):
    backstage_serch_loc = (By.NAME,'order_sn')
    backstage_serch_button_loc = (By.CSS_SELECTOR,'[value=" 搜索 "]')
    status_type_loc = (By.NAME,'status')
    order_click_loc = (By.LINK_TEXT,'查看')

    def backstage_serch(self, order):
        self.find_element(self.backstage_serch_loc).send_keys(order)
        self.select(self.status_type_loc,'待发货')
        self.find_element(self.backstage_serch_button_loc).click()

    def order_click(self):
        self.find_element(self.order_click_loc).click()
        #点击查看，进入操作页面
        sleep(3)














