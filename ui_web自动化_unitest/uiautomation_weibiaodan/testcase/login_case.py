from testcase.test_base import TestBase,exception_monitor
from page.login.login_page import LoginPage
from page.login.main_page import MainPage
from page.login.middle_page import MiddlePage
from page.details_page.goods_details_page import GoodsPage
from page.shopping_cart_page.shopping_cart import ShoppingCart
from page.details_page.order_create_page import CreatOrder
from page.login.login_backstage_page import BackstageLoginPage
from page.details_page.backstage_main_page import Backstage
from page.details_page.backstage_order_list_page import OrderList
from page.details_page.order_success_bage import OrderSuccess
from page.details_page.backstage_order_handle_page import OrderHandle
from page.details_page.delivery_list_page import DeliveryList
from page.details_page.user_center_page import UserCenter
# from DB.DB_base import DBase
from page.details_page.alert_page import Alert
from time import sleep
from ddt import ddt,data,unpack


#import xlrd
# data1 = xlrd.open_workbook(r"C:\Users\30833\Desktop\自动化测试\data.xlsx")
# table =data1.sheet_by_name("login")
# e_list = []
# for n_row in range(1,table.nrows):
#     e_list.append(table.row_values(n_row))
# print(e_list)

import datetime

# def exception_monitor(path):
#     def decorator(func):
#         def wrapper(self, *args, **kw):
#             try:
#                 # 捕获函数异常
#                 return func(self, *args, **kw)
#             except Exception:
#                 s = datetime.datetime.now().strftime('%H_%M_%S')  # 现在
#                 print (s)
#                 # 函数出现异常后的处理
#                 if path.endswith('/'):
#                     self.driver.save_screenshot(path + func.__name__ + '%s_error.png' % s )
#                 else:
#                     self.driver.save_screenshot(path + '/' + func.__name__ + '%s_error.png' % s )
#                     print(path + '/' + func.__name__ + '%s_error.png' % s )
#                 # 为了能在结果展示异常，需要重新抛出该异常
#                 raise
#
#         return wrapper
#
#     return decorator

# @ddt
class LoginCase(TestBase):

    URL = ('http://cwxt.ctce.com.cn:70/')
    # @data(*e_list)
    # @unpack
    @exception_monitor('./results')
    def test_login_success(self):

        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)

        middle_page = MiddlePage(self.driver)


        login_page.open(self.URL)
        # main_page.main_page_login_button()


        login_page.username_input('test05')
        login_page.password_input('A123456&')
        login_page.submit_button()




        alert_success_text = middle_page.alert_login_success()
        self.assertIn('登录成功',alert_success_text,'登录失败!')



    # def test_go_shopping(self):
        main_page = MainPage(self.driver)
        main_page.main_page_goods_select()
        #选择商品
        goodsshooping = GoodsPage(self.driver)
        goodsshooping.goods_sales_button()
        #点击立即购买，进入购物车
        cart = ShoppingCart(self.driver)
        cart.settlement_button()
        #点击结算中心，进入提交订单页
        # order = OrderSuccess(self.driver)

        creat_order = CreatOrder(self.driver)
        creat_order.shipping_way()
        creat_order.payment_way()
        creat_order.pack_way()
        creat_order.card_way()
        creat_order.submit_order()
        # creat_order.count_pay()

        # 订单信息输入，提交订单
        order_run = OrderSuccess(self.driver)
        order_id = order_run.order_number()
        #获取订单号


        login_page.open('http://localhost:8088/upload/admin')
        backstagelogin = BackstageLoginPage(self.driver)
        backstagelogin.username_input('a3664938')
        backstagelogin.password_input('b3664938')
        backstagelogin.submit_button()

        backstage = Backstage(self.driver)
        backstage.frame_to('main-frame')
        #切换进入主页面
        backstage.pending_order_button()
        #进入未发货订单列表
        orderlist = OrderList(self.driver)
        orderlist.backstage_serch(order_id)
        #搜索订单号
        orderlist.order_click()
        #进入订单操作页面
        order_handle = OrderHandle(self.driver)
        # sleep(1)
        order_handle.ship_button()
        # sleep(1)
        #发货确认，并跳转发货列表页
        deliverylist = DeliveryList(self.driver)
        deliverylist.order_serch(order_id)
        sleep(1)
        deliverylist.order_look()
        sleep(1)
        deliverylist.delivery_confirmed()
        sleep(1)
        #完成发货

        backstage.out_frame()
        #跳出主页面
        backstage.frame_to('header-frame')
        sleep(2)
        #跳进头部页面
        backstage.front_desk()
        sleep(2)
        #点击查看网店
        main_page.front()
        sleep(2)
        #跳转到前台页面
        main_page.my_order()

        #点击我的订单
        uc = UserCenter(self.driver)

        uc.my_order_list()
        uc.receiving(order_id)
        sleep(3)
        #收货确认
        alert = Alert(self.driver)
        alert.order_alert()
        sleep(3)



        db = DBase()
        abd = db.serch_data('select user_name,password from ecs_users where user_name=7')
        print(abd)
        sleep(3)

        # creat_order.count_pay()
        sleep(3)




















