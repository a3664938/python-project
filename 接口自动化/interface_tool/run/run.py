# coding:utf-8
from request_method.request_method import RequestMethod
from data_config.operation_excel import OperationExcel
from get_data.get_data import GetDate
from assert_reult.assert_result import AssertResult
from depand_method.depand_method import DdepandMethod
from send_email.send_email import SendEmail


class Run:
    def __init__(self):
        self.request_method=RequestMethod()
        self.opera_excel=OperationExcel()
        self.get_data=GetDate()
        self.assert_result=AssertResult()
        self.send_email=SendEmail()

    def go_run(self):
        lines=self.opera_excel.get_lines()
        pass_case=[]
        fail_case=[]
        for i in range(1,lines):
            res=None
            flag=None
            is_run=self.get_data.get_is_run(i)

            # 判断是否运行
            if is_run == 'yes':
                # 获取必要参数
                method=self.get_data.get_method(i)
                url=self.get_data.get_url(i)
                header=self.get_data.get_header(i)
                data=self.get_data.get_request_data(i)
                depand_id=self.get_data.get_depand_id(i)
                # 判断是否有依赖
                if depand_id:
                    depand_method=DdepandMethod(depand_id)
                    depand_fild=self.get_data.get_depand_fild(i)
                    depand_value=depand_method.get_depand_value(i)
                    if '.'not in depand_fild:
                        header[depand_fild]=depand_value
                    else:
                        denpand_list=depand_fild.split('.')
                        lens=len(denpand_list)
                        if lens==2:
                            header[denpand_list[0]][denpand_list[1]]=depand_value
                        elif lens==3:
                            header[denpand_list[0]][denpand_list[1]][denpand_list[2]] = depand_value
                        elif lens==4:
                            header[denpand_list[0]][denpand_list[1]][denpand_list[2]][denpand_list[3]] = depand_value
                        elif lens==5:
                            header[denpand_list[0]][denpand_list[1]][denpand_list[2]][denpand_list[3]][denpand_list[4]] = depand_value
                        else:
                            print('只支持5层数据')
                            continue
                res=self.request_method.run_main(method,url,header,data)
                # print(i,url,method,res)

                # print(i,url,res)
                # 断言
                except_result=self.get_data.get_expact_result(i)
                assert_result=self.assert_result.assert_contain(except_result,res)
                if assert_result==True:
                    flag='pass'
                    pass_case.append(i)
                else:
                    flag=res
                    fail_case.append(i)

                # 回写测试结果

                self.get_data.write_result(i,flag)

                # print(flag)
        pass_count=len(pass_case)
        fail_count=len(fail_case)

        # 发送测试报告
        if self.get_data.receive_email_account()and self.get_data.send_email_account()and self.get_data.send_email_password()!=None:
            self.send_email.send_report(pass_count,fail_count)
        else:
            print('邮箱信息不完整，本次不会发送邮件')
            pass



if __name__=='__main__':
    run=Run()
    res=run.go_run()


