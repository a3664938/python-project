from page.page_base import Page
from selenium.webdriver.common.by import By
class DataManagePage(Page):
    # =======================================定位器

    # =========【新增】
    add_data_loc=(By.XPATH,'//span[text()="新增"]/..')

    # ========【保存】
    data_save_loc=(By.XPATH,'//span[text()="保存"]/..')

    #========数据输入
    num_root_data1_loc = (By.XPATH, '//span[text()="数字1"]/parent::*/following-sibling::div[1]/div/div/div/span/div/div/div[2]/input')  # 数字1输入
    num_root_data2_loc = (By.XPATH, '//span[text()="数字2"]/parent::*/following-sibling::div[1]/div/div/div/span/div/div/div[2]/input')  # 数字2输入
    num_root_data3_loc = (By.XPATH, '//span[text()="数字3"]/parent::*/following-sibling::div[1]/div/div/div/span/div/div/div[2]/input')  # 数字2输入


    single1_loc = (By.XPATH, '//span[text()="单行文本1"]/parent::*/following-sibling::div[1]/div/div/div/span/div/input')
    module1_loc = (By.XPATH, '//span[text()="多行文本1"]/parent::*/following-sibling::div[1]/div/div/div/span/div/textarea')
    date1_loc = (By.XPATH, '//span[text()="日期时间1"]/parent::*/following-sibling::div[1]/div/div/div/span/div/span/div/input')
    date_now_loc=(By.XPATH,'//a[text()="此刻"]') # 时间控件内的今天


    radio1_loc = (By.XPATH, '//span[text()="单选框1"]/parent::*/following-sibling::div[1]/div/div/div/span/div/div/label[1]/span[2]') # 单选框1
    radio2_loc = (By.XPATH, '//span[text()="单选框1"]/parent::*/following-sibling::div[1]/div/div/div/span/div/div/label[2]/span[2]') # 单选框2
    radio3_loc = (By.XPATH, '//span[text()="单选框1"]/parent::*/following-sibling::div[1]/div/div/div/span/div/div/label[3]/span[2]') # 单选框3

    check1_loc = (By.XPATH, '//span[text()="复选框1"]/parent::*/following-sibling::div[1]/div/div/div/span/div/div/label[1]/span[2]') # 复选框1
    check2_loc = (By.XPATH, '//span[text()="复选框1"]/parent::*/following-sibling::div[1]/div/div/div/span/div/div/label[2]/span[2]') # 复选框2
    check3_loc = (By.XPATH, '//span[text()="复选框1"]/parent::*/following-sibling::div[1]/div/div/div/span/div/div/label[3]/span[2]') # 复选框3

    pulldown1_loc = (By.XPATH, '//span[text()="下拉列表1"]/parent::*/following-sibling::div[1]/div/div/div/span/div/div/div/div')
    pulldown1_data1_loc=(By.CSS_SELECTOR, '[role="listbox"]>li:nth-child(2)') # 下拉选项1
    pulldown1_data2_loc = (By.CSS_SELECTOR, '[role="listbox"]>li:nth-child(3)')  # 下拉选项2
    pulldown1_data3_loc = (By.CSS_SELECTOR, '[role="listbox"]>li:nth-child(4)')  # 下拉选项3


    dropdown1_loc = (By.XPATH, '//span[text()="下拉复选1"]/parent::*/following-sibling::div[1]/div/div/div/span/div/div/div/div')
    dropdown1_data1_loc=(By.XPATH, '/html/body/div[5]/div/div/div/ul/li[1]') # 下拉复选1
    dropdown1_data2_loc = (By.XPATH, '/html/body/div[5]/div/div/div/ul/li[2]')  # 下拉复选2
    dropdown1_data3_loc = (By.XPATH, '/html/body/div[5]/div/div/div/ul/li[3]')  # 下拉复选3


    line1_loc = (By.XPATH, '//span[text()="分割线1"]/../..')
    onoff1_loc = (By.XPATH, '//span[text()="开关1"]/parent::*/following-sibling::div[1]/div/div/div/span/div/button')

    tree1_loc = (By.XPATH, '//span[text()="树形选择1"]/../..')
    data1_loc = (By.XPATH, '//div[text()="关联数据1"]/../..')

    search1_loc = (By.XPATH, '//div[text()="关联查询1"]/../..')

    address1_loc = (By.CSS_SELECTOR, '[placeholder="省/市/区"]')
    address1_beijing_loc=(By.XPATH, '//li[text()="北京市"]')
    address1_shixiaqu_loc = (By.XPATH, '//li[text()="市辖区"]')
    address1_dongchengqu_loc = (By.XPATH, '//li[text()="东城区"]')
    address1_tianjing_loc = (By.XPATH, '//li[text()="天津市"]')
    address1_hepingqu_loc = (By.XPATH, '//li[text()="和平区"]')

    child1_loc = (By.XPATH, '//div[text()="子表单1"]/../..')

    member1_loc = (By.XPATH, '//p[text()="点击选择成员"]')  # 成员控件
    member1_data_loc=(By.XPATH, '//div[text()="cs-1"]') # 选择成员
    member_confirm_loc=(By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div[2]/div/div[4]/div/button[1]') # 确定

    dept1_loc = (By.XPATH, '//p[text()="点击选择部门"]') # 部门控件
    dept1_data_loc = (By.XPATH, '//span[text()="北京中铁物总贸易有限公司"]')  # 选择部门
    dept_confirm_loc = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div[2]/div/div[4]/div/button[1]')  # 确定  这里成员与部门控件的确定键完全相等

    # ==========================================方法
    # =======新增
    def add_data(self):
        self.wait(self.add_data_loc)
        self.find_element(self.add_data_loc).click()


    # =======数据输入

    def time_data1(self):
        self.wait(self.date1_loc)
        self.find_element(self.date1_loc).click()

    def member1(self):
        self.wait(self.member1_loc)
        self.find_element(self.member1_loc).click()

    def member1_data1(self):
        self.wait(self.member1_data_loc)
        self.find_element(self.member1_data_loc).click()


    def num_root_data1(self, values):
        self.wait(self.num_root_data1_loc)
        self.find_element(self.num_root_data1_loc).send_keys(values)

    def num_root_data2(self, values):
        self.wait(self.num_root_data2_loc)
        self.find_element(self.num_root_data2_loc).send_keys(values)

    def num_root_data3(self, values):
        self.wait(self.num_root_data3_loc)
        self.find_element(self.num_root_data3_loc).send_keys(values)

