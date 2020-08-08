from page.page_base import Page
from selenium.webdriver.common.by import By

class UserCenter(Page):
    user_center_loc = (By.CSS_SELECTOR,'[href="user.php?act=order_list"]')


    def my_order_list(self):
        self.wait(self.user_center_loc)
        self.find_element(self.user_center_loc).click()

        #点击我的订单，展开订单列表

    def receiving(self,order):
        self.find_element((By.XPATH,"//a[text()=%s]/../../td[5]"%order)).click()
