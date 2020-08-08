from page.page_base import Page
from selenium.webdriver.common.by import By



class MainPage(Page):

    login_button_loc = (By.LINK_TEXT, '登录')
    goods_select_loc = (By.CSS_SELECTOR,'#show_hot_area>:nth-child(1)>:nth-child(1)')
    my_order_loc = (By.CSS_SELECTOR,'[href="user.php"]')



    # alert_login_success_div_loc = (By.CSS_SELECTOR,'.alert.alert-success')
    # def alert_login_sucess_div(self):
    #     self.wait(self.alert_login_success_div_loc)
    #     return self.find_element(self.alert_login_success_div_loc).text

    def main_page_login_button(self):
        self.find_element(self.login_button_loc).click()

    def main_page_goods_select(self):
        self.find_element(self.goods_select_loc).click()

    def front(self):
        self.switch_to_window()
        #切换到新开页面
        
    def my_order(self):
        self.find_element(self.my_order_loc).click()
        #跳转用户中心
