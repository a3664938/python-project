# coding=utf-8
import unittest
from HTMLTestRunner.HTMLTestRunner.HTMLTestRunner_PY3 import HTMLTestRunner
from config import DIR
import os

# num=int(input("请输入："))
#
# for i in range(num):
#
#     i += 1
#     print(i)
discover = unittest.defaultTestLoader.discover(
    start_dir=DIR + os.path.sep + 'testcase',
    pattern='*case.py'
)

# runner = unittest.TextTestRunner()
# runner.run(discover)

# 生成html报告运行
with open(DIR + os.path.sep +'results/report.html','wb')as f:
    runner = HTMLTestRunner(
        stream=f,
        title='CRM自动化测试',
        description='win10,Chrome',

    )
    runner.run(discover)

