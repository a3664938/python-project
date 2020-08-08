import datetime
from testcase.test_base import TestBase,exception_monitor

from page.form_page.list_page import ListPage
from page.form_page.Design_page import DesignPage
from time import sleep
from page.form_page.allocation_right_page import AllocationRightPage



class FormCase(TestBase):

    url='http://cd.sysdsoft.cn:10003/#/formViewList?userId=475FC3FA-9833-416D-A1C5-E1E885E24C23&userOrgDutyId=90BF1987-E638-42BB-B491-69EF774FF1FD&feopapi1=userOrgDutyId,userId,platform&feopapi2=userOrgDutyId,userId&platform=NPF'

    @exception_monitor('./results')
    def test_list(self):

        listpage=ListPage(self.driver)
        rightpage = AllocationRightPage(self.driver)
        designpage=DesignPage(self.driver)
        listpage.open(self.url)
        sleep(3)
        listpage.build_form()
        sleep(3)
        designpage.card_container()
        sleep(3)

        rightpage.search_allocation_right()
        designpage.text_single()

        designpage.address_field()


