# coding=utf-8
from page.page_base import Page
from selenium.webdriver.common.by import By
class AllocationRightPage(Page):
    # ==========定位器

    # =======选择部分成员
    search_loc=(By.CSS_SELECTOR, ".anticon-search > svg")
    search_send_keys_loc=(By.CSS_SELECTOR, ".ant-input-search > .ant-input")
    select_role_loc=(By.XPATH,'//div[text()="系统管理员"]/div')

    # ========操作权限
    add_loc=(By.XPATH,'//span[text()="添加"]/preceding-sibling::*')

    # ========字段权限
    field_permissions_loc=(By.XPATH,'//div[text()="字段权限"]')
    editable_loc=(By.XPATH,'//*[@id="Boots"]/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div[3]/div[3]/label/span/input')

    # ========权限保存
    allocation_right_save_loc=(By.XPATH,'//span[text()="保 存"]/..')

    # ========跳转“数据管理”
    data_manage_loc=(By.XPATH,'//span[text()="数据管理"]')


    def search_allocation_right(self):
        self.wait(self.search_loc)
        self.find_element(self.search_loc).click()
    def seatch_sendkeys(self,values):
        self.wait(self.search_send_keys_loc)
        self.find_element(self.search_send_keys_loc).send_keys(values)
    def select_role(self):
        self.wait(self.select_role_loc)
        self.find_element(self.select_role_loc).click()
    def add_right(self):
        self.wait(self.add_loc)
        self.find_element(self.add_loc).click()
    def field_permissions(self):
        self.wait(self.field_permissions_loc)
        self.find_element(self.field_permissions_loc).click()

    def editable(self):
        self.wait(self.editable_loc)
        self.find_element(self.editable_loc).click()
    def allocation_right_save(self):
        self.wait(self.allocation_right_save_loc)
        self.find_element(self.allocation_right_save_loc).click()
    def data_manage(self):
        self.wait(self.data_manage_loc)
        self.find_element(self.data_manage_loc).click()