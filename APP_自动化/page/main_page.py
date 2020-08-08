from page.page_base import Page


class MainPage(Page):

    def my(self):
        self.wait_activity('.ui.main.MainActivity')
        self.tap_click(633,1218)

        #点击【我的】

    def good_select(self):

        self.tap_click(59, 698)
        # 购买商品，进入限时促销页面
