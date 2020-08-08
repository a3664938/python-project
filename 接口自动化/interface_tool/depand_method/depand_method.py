# coding:utf-8
from data_config.operation_excel import OperationExcel
from get_data.get_data import GetDate
from request_method.request_method import RequestMethod
from jsonpath_rw import jsonpath,parse
import json
class DdepandMethod:
    def __init__(self,case_id):
        self.opera_excel=OperationExcel()
        self.request_method=RequestMethod()
        self.get_data=GetDate()
        self.case_id=case_id
        self.row = self.opera_excel.depand_row(case_id)

    def go_depand_run(self):

        method=self.get_data.get_method(self.row)
        url=self.get_data.get_url(self.row)
        header=self.get_data.get_header(self.row)
        data=self.get_data.get_request_data(self.row)
        res=json.loads(self.request_method.run_main(method=method,url=url,header=header,data=data))
        return res

    # 获取依赖值
    def get_depand_value(self,row):
        data=self.go_depand_run()
        depand_data=self.get_data.get_depand_data(row)
        json_exe=parse(depand_data)
        madle=json_exe.find(data)
        res=[math.value for math in madle][0]
        return res



if __name__ == '__main__':
    run=DdepandMethod('imooc-001')
    res=run.get_depand_value(2)
    print(res)