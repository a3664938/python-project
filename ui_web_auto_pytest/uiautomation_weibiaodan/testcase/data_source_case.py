import datetime
from testcase.test_base import TestBase,exception_monitor # 导包可以导入函数，这里将装饰器放在测试基类里，方便调用
from page.form_page.list_page import ListPage
from page.form_page.Design_page import DesignPage
from page.form_page.allocation_right_page import AllocationRightPage
from page.form_page.data_manage_page import DataManagePage
from time import sleep
class Data_Source_Case(TestBase):

    url='http://cd.sysdsoft.cn:10003/#/formViewList?userId=475FC3FA-9833-416D-A1C5-E1E885E24C23&userOrgDutyId=90BF1987-E638-42BB-B491-69EF774FF1FD&feopapi1=userOrgDutyId,userId,platform&feopapi2=userOrgDutyId,userId&platform=NPF'

    @exception_monitor('./results')
    def test_data_source(self):
        listpage=ListPage(self.driver)
        listpage.open(self.url)
        sleep(3)
        listpage.build_form()
        designpage = DesignPage(self.driver)
        designpage.form_rename('自动化测试')
        designpage.card_container()
        designpage.card_container1()
        designpage.text_single()
        designpage.text_module()
        designpage.date_field()
        designpage.num_field()
        designpage.accessory_field()
        designpage.radio_button()
        designpage.check_box()
        designpage.pulldown_list()
        designpage.dropdown_check()
        designpage.cross_line()
        designpage.on_off()
        designpage.tree_selection()
        designpage.serial_num()
        designpage.address_field()
        designpage.member_field()
        designpage.dept_field()
        designpage.form_save()
        print('完成表单设计')
        sleep(3)
        print('开始分配权限')
        sleep(3)
        designpage.allocation_right()
        print('点击“分配选项”')
        rightpage=AllocationRightPage(self.driver)

        sleep(4)
        rightpage.search_allocation_right()
        sleep(3)
        rightpage.seatch_sendkeys('系统管理员')
        sleep(1)
        rightpage.select_role()
        sleep(1000)
        rightpage.add_right()
        sleep(1000)
        rightpage.field_permissions()
        sleep(1000)
        rightpage.editable()
        rightpage.allocation_right_save()
        sleep(3000)
        rightpage.data_manage()
        sleep(3000)
        data=DataManagePage(self.driver)
        data.add


