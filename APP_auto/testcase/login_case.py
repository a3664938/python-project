from testcase.test_base import TestBase
from page.main_page import MainPage
from page.uesr_page import UserPage
from page.login_page import Logining
from page.promotion_page import Promotion
from page.goods_page import Goods
from page.order_page import OrderList
from page.checkstand_page import Checkstand
from page.pay_page import Pay
from page.my_order_page import MyOrder
from page.set_page import SetPage
from time import sleep
class LongCase(TestBase):

    def test_login(self):

        mainpage = MainPage(self.driver)
        sleep(2)
        mainpage.my()
        #进入我的

        userpage = UserPage(self.driver)

        userpage.login_button()
        #点击登录,跳转登录页

        logining = Logining(self.driver)
        logining.username('13982101584')
        logining.password('b3664938')
        logining.login()
        # 登录成功

        # img = self.driver.get_screenshot_as_base64()
        # string = """
        # <!DOCTYPE html>
        # <html lang="en">
        # <head>
        #     <meta charset="UTF-8">
        #     <title>Title</title>
        # </head>
        # <body>
        #     <div id="img">
        #     <img src="data:image/png;base64,%s">
        #     </div>
        # </body>
        # </html>
        # """ % img
        # with open(r'C:\Users\30833\Desktop\d盘\t.html', 'w', encoding='utf-8') as f:
        #     f.write(string)

        self.driver.save_screenshot('/results/login.png')


        username = userpage.login_success()
        self.assertIn('13982101584',username,'登录失败')


        userpage.main_page_button()
        #点击首页
        sleep(2)

        mainpage.good_select()
        # 购买商品，进入限时促销页面

        promotion = Promotion(self.driver)
        sleep(1)
        promotion.go_buy()
        # 进入商品页

        goods = Goods(self.driver)
        sleep(1)
        goods.buy_button()
        # 点击购买，进入订单页

        orderlist = OrderList(self.driver)
        orderlist.submit_order()
        # 提交订单,跳转收银台

        checkstand = Checkstand(self.driver)
        sleep(1)
        checkstand.pay_way()
        checkstand.pay_affirm()
        # 进入支付页

        pay = Pay(self.driver)
        pay.pay_cancel()
        pay.pay_cancel_affirm()
        # 确认取消支付
        pay.back()
        # 返回至商品页

        goods.back()
        # 点击返回，返回至促销页

        promotion.back()
        sleep(1)
        # 返回到首页

        mainpage.my()

        # 进入我的
        userpage.non_payment()

        #点击进入我的未付款订单

        myorder = MyOrder(self.driver)
        myorder.order_cancel()
        # 取消订单
        myorder.cancle_affirm()

        # 确定取消订单
        # toast = self.driver.find_element_by_xpath('//*[@text="取消订单成功！"]')
        # print (toast)
        myorder.back()
        # 返回上一页

        userpage.set()
        # 点击设置,进入设置页面

        setpage = SetPage(self.driver)
        setpage.logout()
        setpage.logout_affirm()
        # 点击退出登录









