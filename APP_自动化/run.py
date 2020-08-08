import unittest
from HTMLTestRunner import HTMLTestRunner
discover = unittest.defaultTestLoader.discover(
    start_dir='testcase',
    pattern='*case.py'
)
# with open('results/report.html','wb')as f:
#     runner = HTMLTestRunner(
#         stream=f,
#         title='CRM自动化测试',
#         description='win10,Chrome',
#         tester='nemo'
#     )
#     runner.run(discover)

runner = unittest.TextTestRunner()
runner.run(discover)