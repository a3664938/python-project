# coding:utf-8
class AssertResult:
    def assert_contain(self,one_data,two_data):
        flag=None
        if one_data in two_data:
            flag=True
        else:
            flag=False
        return flag
