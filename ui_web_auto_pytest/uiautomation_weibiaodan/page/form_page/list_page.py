from page.page_base import Page
from selenium.webdriver.common.by import By
class ListPage(Page):

    newbuild_loc=(By.XPATH,'//span[text()="新增表单"]/..')    # 新建表单
    newbuildflow_loc=(By.XPATH,'//span[text()="新增流程表单"]/..')   # 新建流程表单
    search_loc=(By.CSS_SELECTOR,'input[placeholder="请输入模板名称查询"]')  #输入搜索关键词
    unfold_loc=(By.XPATH,'//div[text()="版2020.03.11"]/../../td/div')   #展开模板
    versions_loc=(By.CSS_SELECTOR,'#root > div > div.src-components-DataManage-TableCom__contentTable--gHJws > div > div > div > div > div > div > div.ant-table-body > table > tbody > tr.ant-table-expanded-row.ant-table-expanded-row-level-1 > td:nth-child(2) > div > div > div > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > div:nth-child(1) > span')

    def build_form(self):
        self.wait(self.newbuild_loc)
        self.find_element(self.newbuild_loc).click()
    def build_formflow(self):
        self.wait(self.newbuildflow_loc)
        self.find_element(self.newbuildflow_loc).click()
    def search_template(self,values):
        self.wait(self.search_loc)
        self.find_element(self.search_loc).send_keys('values')
    def template_unfold(self):
        self.wait(self.unfold_loc)
        self.find_element(self.unfold_loc).click()
    def select_versions(self):
        self.find_element(self.versions_loc).click()





