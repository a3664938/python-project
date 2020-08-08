# coding:utf-8
from data_config.operation_excel import OperationExcel
import json
class GetDate:
    def __init__(self):
        self.opera_excel=OperationExcel()
        self.opera_excel_email=OperationExcel(sheet_id=1)

    # 获取case_id
    def get_case_id(self,row):
        case_id=self.opera_excel.get_cell_value(row,0)
        return case_id

    # 获取url
    def get_url(self,row):
        url = self.opera_excel.get_cell_value(row, 2)
        return url

    # 获取是否执行
    def get_is_run(self,row):
        is_run = self.opera_excel.get_cell_value(row, 3).lower()
        return is_run

    # 获取请求方式
    def get_method(self,row):
        method = self.opera_excel.get_cell_value(row, 4)
        return method

    # 获取header
    def get_header(self,row):
        header = self.opera_excel.get_cell_value(row, 5)
        if header:
            header=json.loads(header)
        return header

    # 获取依赖id
    def get_depand_id(self,row):
        depand_id = self.opera_excel.get_cell_value(row, 6)
        return depand_id

    # 获取依赖数据规则
    def get_depand_data(self,row):
        depand_data = self.opera_excel.get_cell_value(row, 7)
        return depand_data

    # 获取依赖数据所属字段
    def get_depand_fild(self,row):
        depand_fild = self.opera_excel.get_cell_value(row, 8)
        return depand_fild

    # 获取请求数据
    def get_request_data(self,row):
        request_data = self.opera_excel.get_cell_value(row, 9)
        if request_data:
            return json.loads(request_data) # 获取的str数据转字典

    # 获取预期结果
    def get_expact_result(self,row):
        expact_result = self.opera_excel.get_cell_value(row, 10)
        return expact_result

    # 获取结果
    def get_result(self,row):
        result = self.opera_excel.get_cell_value(row, 11)
        return result

    # 回写测试结果
    def write_result(self,row,value):
        self.opera_excel.write_excel(row,11,value)
        print('第%d行测试结果已回写excle中'%row)

    #===============================# 获取邮件信息

    # 获取邮箱服务器
    def email_server(self):
        email_server=self.opera_excel_email.get_cell_value(1,0)
        return email_server

    # 获取发送邮箱账号
    def send_email_account(self):
        send_email_account=self.opera_excel_email.get_cell_value(1,1)
        return send_email_account

    # 获取发送邮箱密码
    def send_email_password(self):
        send_email_password=self.opera_excel_email.get_cell_value(1,2)
        return send_email_password

    # 获取收件箱
    def receive_email_account(self):
        receive_email_account=self.opera_excel_email.get_cell_value(1,3)
        return receive_email_account