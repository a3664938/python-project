# coding=utf-8
from page.page_base import Page
from selenium.webdriver.common.by import By
import datetime
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
class DesignPage(Page):
    # ====================================定位器

    # ========表单标题
    form_name_loc = (By.CSS_SELECTOR, 'input[placeholder="表单名称"]')  # 表单名称

    # =======表单设计页面【预览】【保存】【发布】【分配权限】
    form_preview_loc=(By.XPATH,'//div[text()="预览"]')
    form_save_loc=(By.XPATH,'//div[text()="保存"]')
    form_publish_loc=(By.XPATH,'//div[text()="发布"]')
    allocation_right_loc=(By.XPATH,'//div[text()="分配权限"]')

    # ========左侧控件区域(功能区)
    card_loc=(By.XPATH,'//div[text()="卡片容器"]')   #卡片容器
    tag_loc=(By.XPATH,'//div[text()="标签容器"]')   #标签容器
    single_loc=(By.XPATH,'//div[text()="单行文本"]')
    module_loc=(By.XPATH,'//div[text()="多行文本"]')
    date_loc=(By.XPATH,'//div[text()="日期时间"]')
    num_loc=(By.XPATH,'//div[text()="数字"]')
    accessory_loc=(By.XPATH,'//div[text()="附件"]')
    radio_loc=(By.XPATH,'//div[text()="单选框"]')
    check_loc=(By.XPATH,'//div[text()="复选框"]')
    pulldown_loc=(By.XPATH,'//div[text()="下拉列表"]')
    dropdown_loc=(By.XPATH,'//div[text()="下拉复选"]')
    line_loc=(By.XPATH,'//div[text()="分割线"]')
    onoff_loc=(By.XPATH,'//div[text()="开关"]')
    tree_loc=(By.XPATH,'//div[text()="树形选择"]')
    data_loc=(By.XPATH,'//div[text()="关联数据"]')
    serial_loc=(By.XPATH,'//div[text()="流水号"]')
    search_loc=(By.XPATH,'//div[text()="关联查询"]')
    address_loc=(By.XPATH,'//div[text()="地址"]')
    child_loc=(By.XPATH,'//div[text()="子表单"]')
    member_loc=(By.XPATH,'//div[text()="成员组件"]')
    dept_loc=(By.XPATH,'//div[text()="部门组件"]')

    # 中间设计区域
    card1_loc=(By.XPATH,'//div[text()="卡片容器1"]')   #卡片容器1
    tag1_loc=(By.XPATH,'//div[text()="标签页1"]')   #标签容器1
    single1_loc = (By.XPATH, '//span[text()="单行文本1"]/../..')
    module1_loc=(By.XPATH,'//span[text()="多行文本1"]/../..')
    date1_loc=(By.XPATH,'//span[text()="日期时间1"]/../..')
    num1_loc=(By.XPATH,'//span[text()="数字1"]/../..')
    accessory1_loc=(By.XPATH,'//div[text()="附件1"]/../..')
    radio1_loc=(By.XPATH,'//span[text()="单选框1"]/../..')
    check1_loc=(By.XPATH,'//span[text()="复选框1"]/../..')
    pulldown1_loc=(By.XPATH,'//span[text()="下拉列表1"]/../..')
    dropdown1_loc=(By.XPATH,'//span[text()="下拉复选1"]/../..')
    line1_loc=(By.XPATH,'//span[text()="分割线1"]/../..')
    onoff1_loc=(By.XPATH,'//span[text()="开关1"]/../..')
    tree1_loc=(By.XPATH,'//span[text()="树形选择1"]/../..')
    data1_loc=(By.XPATH,'//div[text()="关联数据1"]/../..')
    serial1_loc=(By.XPATH,'//span[text()="流水号1"]/../..')
    search1_loc=(By.XPATH,'//div[text()="关联查询1"]/../..')
    address1_loc=(By.XPATH,'//span[text()="地址1"]/../..')
    child1_loc=(By.XPATH,'//div[text()="子表单1"]/../..')
    member1_loc=(By.XPATH,'//span[text()="成员组件1"]/../..')
    dept1_loc=(By.XPATH,'//span[text()="部门组件1"]/../..')

    # 子表内控件区域
    singlechild1_loc=(By.XPATH, '//div[text()="单行文本1"]/../..')  # 与中间区域（主表控件）相比，只是标签由span变为了div
    singlechild2_loc = (By.XPATH, '//div[text()="单行文本1"]/../..')
    plusbuton_loc=(By.XPATH, '//div[text()="子表单1"]/following-sibling::div[1]/div/div/div/div/div/div/div[2]/div/div/table/thead/tr/th[2]/span/div/span[1]/a') # 子表内“+”号
    singlechild1_data_loc=(By.XPATH, '//div[text()="子表单1"]/following-sibling::div[1]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/div/div/div/span/input') # 子表内单行文本1第一行数据
    singlechild1_data2_loc = (By.XPATH,'//div[text()="子表单1"]/following-sibling::div[1]/div/div/div/div/div/div/div[1]/div/table/tbody/tr[2]/td[3]/div/div/div/span/input')  # 子表内单行文本1第二行数据
    singlechild2_data_loc = (By.XPATH,'//div[text()="子表单1"]/following-sibling::div[1]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[4]/div/div/div/span/input') # 子表内单行文本2第一行数据
    singlechild2_data2_loc = (By.XPATH,'//div[text()="子表单1"]/following-sibling::div[1]/div/div/div/div/div/div/div[1]/div/table/tbody/tr[2]/td[4]/div/div/div/span/input')  # 子表内单行文本2第二行数据
    numchild1_data1_loc = (By.XPATH,'//div[text()="子表单1"]/following-sibling::div[1]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/div/div/div/span/div/div[2]/input')  # 子表内数字控件1第一行数据
    numchild1_data2_loc = (By.XPATH,'//div[text()="子表单1"]/following-sibling::div[1]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[4]/div/div/div/span/div/div[2]/input')  # 子表内数字控件2第一行数据
    numchild2_data1_loc = (By.XPATH,'//div[text()="子表单1"]/following-sibling::div[1]/div/div/div/div/div/div/div[1]/div/table/tbody/tr[2]/td[3]/div/div/div/span/div/div[2]/input')  # 子表内数字控件2第一行数据
    numchild2_data2_loc = (By.XPATH,'//div[text()="子表单1"]/following-sibling::div[1]/div/div/div/div/div/div/div[1]/div/table/tbody/tr[2]/td[4]/div/div/div/span/div/div[2]/input')  # 子表内数字控件2第一行数据




    right_buton_loc=(By.XPATH,'//div[text()="子表单1"]/following-sibling::div[1]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[5]/a[1]/i') # 子表数据第一行确认键“勾”
    right_buton2_loc = (By.XPATH,'//div[text()="子表单1"]/following-sibling::div[1]/div/div/div/div/div/div/div[1]/div/table/tbody/tr[2]/td[5]/a[1]/i')  # 子表数据第二行确认键“勾”
    # 右侧属性区域
    # 默认值/选项
    default_loc = (By.XPATH, '//div[text()="自定义"]/../..')
    datalink_loc = (By.XPATH, '//li[text()="公式编辑"]/../..')
    third_loc = (By.XPATH, '//li[text()="关联第三方数据源"]/../..')
    formula_loc = (By.XPATH, '//li[text()="公式编辑"]/../..')
    other_loc = (By.XPATH, '//li[text()="关联其他表单数据"]/../..')

    # =====关联表
    linkform_loc = (By.XPATH, '//span[text()="关联表"]/../../div[2]') # 关联表
    searchlinkform_loc=(By.XPATH,'// span[text() = "关联表"] /../../ div[2] / div / div / div / div / div / input') # 搜索表


    # ======公式编辑框
    textarea_loc=(By.CSS_SELECTOR,'textarea') # 这个定位比较难准确定位，用的IDE录制脚本的方式才成功定位的
    # 表单字段
    gs_num2_loc=(By.XPATH,'//div[text()="子表单1.数字2"]') # 不同的字段，只需要修改不同得text名称就好了
    gs_num3_loc = (By.XPATH, '//div[text()="子表单1.数字3"]')



    # ===========方法--左侧控件区域

    # ========表单标题
    def form_rename(self,values):
        self.wait(self.form_name_loc)
        self.find_element(self.form_name_loc).clear()
        sleep(1)
        self.find_element(self.form_name_loc).send_keys('%s-%s'%(values,datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')))

    # ========表单【预览】【保存】【发布】
    def form_preview(self):
        self.wait(self.form_preview_loc)
        self.find_element(self.form_preview_loc).click()
    def form_save(self):
        self.wait(self.form_save_loc)
        self.find_element(self.form_save_loc).click()
    def form_publish(self):
        self.wait(self.form_publish_loc)
        self.find_element(self.form_publish_loc).click()
    def allocation_right(self):
        self.wait(self.allocation_right_loc)
        self.find_element(self.allocation_right_loc).click()

    # ========左侧控件区域
    def card_container(self):
        self.wait(self.card_loc)
        self.find_element(self.card_loc).click()
    def card_tag(self):
        self.wait(self.tag_loc)
        self.find_element(self.tag_loc).click()
    def text_single(self):
        self.wait(self.single_loc)
        self.find_element(self.single_loc).click()
    def text_module(self):
        self.wait(self.module_loc)
        self.find_element(self.module_loc).click()
    def date_field(self):
        self.wait(self.date_loc)
        self.find_element(self.date_loc).click()
    def num_field(self):
        self.wait(self.num_loc)
        self.find_element(self.num_loc).click()
    def accessory_field(self):
        self.wait(self.accessory_loc)
        self.find_element(self.accessory_loc).click()
    def radio_button(self):
        self.wait(self.radio_loc)
        self.find_element(self.radio_loc).click()
    def check_box (self):
        self.wait(self.check_loc)
        self.find_element(self.check_loc).click()
    def pulldown_list (self):
        self.wait(self.pulldown_loc)
        self.find_element(self.pulldown_loc).click()
    def dropdown_check (self):
        self.wait(self.dropdown_loc)
        self.find_element(self.dropdown_loc).click()
    def cross_line (self):
        self.wait(self.line_loc)
        self.find_element(self.line_loc).click()
    def on_off (self):
        self.wait(self.onoff_loc)
        self.find_element(self.onoff_loc).click()
    def tree_selection (self):
        self.wait(self.tree_loc)
        self.find_element(self.tree_loc).click()
    def data_associated (self):
        self.wait(self.data_loc)
        self.find_element(self.data_loc).click()
    def search_associated (self):
        self.wait(self.search_loc)
        self.find_element(self.search_loc).click()
    def serial_num (self):
        self.wait(self.serial_loc)
        self.find_element(self.serial_loc).click()
    def address_field (self):
        self.wait(self.address_loc)
        self.find_element(self.address_loc).click()
    def child_form (self):
        self.wait(self.child_loc)
        self.find_element(self.child_loc).click()
    def member_field (self):
        self.wait(self.member_loc)
        self.find_element(self.member_loc).click()
    def dept_field (self):
        self.wait(self.dept_loc)
        self.find_element(self.dept_loc).click()


    # 方法--中间设计区域
    def card_container1(self):
        self.wait(self.card1_loc)
        self.find_element(self.card1_loc).click()
    def card_tag1(self):
        self.wait(self.tag1_loc)
        self.find_element(self.tag1_loc).click()
    def text_single1(self):
        self.wait(self.single1_loc)
        self.find_element(self.single1_loc).click()
    def text_module1(self):
        self.wait(self.module1_loc)
        self.find_element(self.module1_loc).click()
    def date_field1(self):
        self.wait(self.date1_loc)
        self.find_element(self.date1_loc).click()
    def num_field1(self):
        self.wait(self.num1_loc)
        self.find_element(self.num1_loc).click()
    def accessory_field1(self):
        self.wait(self.accessory1_loc)
        self.find_element(self.accessory1_loc).click()
    def radio_button1(self):
        self.wait(self.radio1_loc)
        self.find_element(self.radio1_loc).click()
    def check_box1(self):
        self.wait(self.check1_loc)
        self.find_element(self.check1_loc).click()
    def pulldown_list1 (self):
        self.wait(self.pulldown1_loc)
        self.find_element(self.pulldown1_loc).click()
    def dropdown_check1 (self):
        self.wait(self.dropdown1_loc)
        self.find_element(self.dropdown1_loc).click()
    def cross_line1 (self):
        self.wait(self.line1_loc)
        self.find_element(self.line1_loc).click()
    def on_off1 (self):
        self.wait(self.onoff1_loc)
        self.find_element(self.onoff1_loc).click()
    def tree_selection1 (self):
        self.wait(self.tree1_loc)
        self.find_element(self.tree1_loc).click()
    def data_associated1 (self):
        self.wait(self.data1_loc)
        self.find_element(self.data1_loc).click()
    def search_associated1 (self):
        self.wait(self.search1_loc)
        self.find_element(self.search1_loc).click()
    def serial_num1 (self):
        self.wait(self.serial1_loc)
        self.find_element(self.serial1_loc).click()
    def address_field1 (self):
        self.wait(self.address1_loc)
        self.find_element(self.address1_loc).click()
    def child_form1 (self):
        self.wait(self.child1_loc)
        self.find_element(self.child1_loc).click()
    def member_field1 (self):
        self.wait(self.member1_loc)
        self.find_element(self.member1_loc).click()
    def dept_field1 (self):
        self.wait(self.dept1_loc)
        self.find_element(self.dept1_loc).click()

    # ======子表内控件区域
    def text_singlechild1(self):
        self.wait(self.singlechild1_loc)
        self.find_element(self.singlechild1_loc).click()
    def text_singlechild2(self):
        self.wait(self.singlechild2_loc)
        self.find_element(self.singlechild2_loc).click()
    def text_singlechild1_data(self,values):
        self.wait(self.singlechild1_data_loc)
        self.find_element(self.singlechild1_data_loc).send_keys(values)
    def text_singlechild1_data2(self,values):
        self.wait(self.singlechild1_data2_loc)
        self.find_element(self.singlechild1_data2_loc).send_keys(values)
    def text_singlechild2_data(self, values):
        self.wait(self.singlechild2_data_loc)
        self.find_element(self.singlechild2_data_loc).send_keys(values)

    def text_singlechild2_data2(self, values):
        self.wait(self.singlechild2_data2_loc)
        self.find_element(self.singlechild2_data2_loc).send_keys(values)
    def right_buton1(self):
        self.wait(self.right_buton_loc)
        self.find_element(self.right_buton_loc).click()
    def right_buton2(self):
        self.wait(self.right_buton2_loc)
        self.find_element(self.right_buton2_loc).click()

    # =======右侧属性区域
    # =======默认值/选项
    def default_values(self): # 点击默认值
        self.wait(self.default_loc)
        self.find_element(self.default_loc).click()
    def datalink_values(self): # 选择数据联动
        self.wait(self.datalink_loc)
        self.find_element(self.datalink_loc).click()
    def third_values(self): # 关联第三方数据源
        self.wait(self.third_loc)
        self.find_element(self.third_loc).click()
    def formula_values(self): # 公式编辑
        self.wait(self.formula_loc)
        self.find_element(self.formula_loc).click()
    def other_values(self): # 关联其他表单数据
        self.wait(self.other_loc)
        self.find_element(self.other_loc).click()

    # ======关联表
    def link_form(self): # 点击“关联表”
        self.wait(self.linkform_loc)
        self.find_element(self.linkform_loc).click()
    def search_linkform(self,values): # 搜索表
        self.wait(self.searchlinkform_loc)
        self.find_element(self.searchlinkform_loc).send_keys(values)
    def enter(self): # 回车
        self.keys_enter(self.linkform_loc)

