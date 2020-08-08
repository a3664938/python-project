from page.page_base import Page
from selenium.webdriver.common.by import By
from time import sleep

class MyOrder(Page):
    order_cancel_loc = (By.ID,'cn.tfb.msshop:id/btn_two')
    cancle_affirm_loc = (By.XPATH,'//*[@text="确定"]')

    def order_cancel(self):
        self.wait_activity('.ui.mine.MineOrderActivity')
        self.find_element(self.order_cancel_loc).click()
        #取消订单

    def cancle_affirm(self):
        self.wait(self.cancle_affirm_loc)
        self.find_element(self.cancle_affirm_loc).click()
        #确定取消

    def back(self):
        sleep(1)
        self.driver.keyevent('4')
        #返回上一页

