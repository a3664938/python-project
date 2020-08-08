from testcase.test_base import TestBase
from page.login.login_page import LoginPage
from page.page_base import Page
from selenium.webdriver.common.by import By


class GoodsPage(Page):

    goods_inventory_loc = (By.CSS_SELECTOR,'form#ECS_FORMBUY>:nth-child(3)>:nth-child(3)>dd')
    goods_shop_price_loc = (By.ID,'ECS_SHOPPRICE')
    goods_sales_price_loc = (By.CSS_SELECTOR,'.padd.loop>:nth-child(2)')
    goods_name_loc = (By.CSS_SELECTOR,'h1.clearfix')
    goods_sale_button = (By.CSS_SELECTOR,'[src="themes/ecmoban_meilishuo/images/goumai2.gif"]')
    #定位器
    def goods_inventory(self):
        return self.find_element(self.goods_inventory_loc).text[-2:]

    def goods_price(self):
        return self.find_element(self.goods_shop_price_loc).text[1:-1]

    def goods_sale_price(self):
        return self.find_element(self.goods_sales_price_loc).text[1:-1]

    def goods_name(self):
        return self.find_element(self.goods_name_loc).text

    def goods_sales_button(self):
        self.find_element(self.goods_sale_button).click()





