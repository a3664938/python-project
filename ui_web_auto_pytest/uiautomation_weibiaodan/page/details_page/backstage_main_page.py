from page.page_base import Page
from selenium.webdriver.common.by import By

class Backstage(Page):
    frame_main_loc  = ('main-frame')
    pending_order_loc = (By.LINK_TEXT,'待发货订单:')
    front_desk_loc = (By.LINK_TEXT,'查看网店')

    def frame_to(self,a):
        self.switch_to_frame(a)
        #跳转frame

    def pending_order_button(self):
        self.find_element(self.pending_order_loc).click()
        #点击待发货订单

    def out_frame(self):
        self.switch_to_default()
        #跳出到最外层

    def front_desk(self):
        self.find_element(self.front_desk_loc).click()
        #点击查看网页


