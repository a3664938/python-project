作者：盲
qq:308333575

这是一个python开发的接口自动化工具：
1.用excel管理用例，测试结束后，测试结果自动回写excel。
2.支持具有依赖性用例的测试。
3.运行结束后，自动通过邮件发送测试结果。
4.开放源码，可自行学习及修改，增加功能。

使用方法：
1.用例及邮箱设置（data/interface.xls）
2.运行用例（run/run.py）

F&Q:
1.需要先安装python3.6以上版本（含）
2.确认此工程运用到的第三方库已安装（requests，jsonpath_rw，xlrd，xlwt，xlutils）