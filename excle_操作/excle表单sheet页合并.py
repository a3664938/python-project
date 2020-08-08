# conding:utf-8
"""
表单A中有10个sheet页，表单B中有10个sheet页，现在需要将B中的10个sheet合并到A中，使A中有20个sheet页
"""
import xlrd
import xlwt
from xlutils.copy import copy

def write_sheet_xls(path1, path2):
    # path1 需要合并的表单，path2 被合并的表单
    # 现有表单基础上，新建sheet的时候进行调用
    with xlrd.open_workbook(path2) as wb: # 打开被合并的表单
        sheet_names = wb.sheet_names()  # 获取需要合并的表单的所有sheet名称
        for sheet_name in sheet_names:  # 根据sheet名称循环写入目标表单
            ws = wb.sheet_by_name(sheet_name)  # 根据sheet名称获取sheet内容
            rb = xlrd.open_workbook(path1)  # 打开目标表单
            ws2 = copy(rb)  # 复制目标表单所有数据
            if sheet_name not in rb.sheet_names(): # 如果目标表单中无需要合并表单的sheet时，才执行合并操作
                ws3 = ws2.add_sheet(sheet_name)  # 在目标表单中新建一个sheet
                lines = ws.nrows  # 获取sheet里数据的行数
                for i in range(0, lines): # 写入数据
                    for j in range(0, len(ws.row_values(i))):
                        ws3.write(i, j, ws.cell_value(i,j))  # 向表格中写入数据（对应的行和列）
                ws2.save(path1)  # 保存工作簿
    print("xls格式表格写入数据成功！")

if __name__=='__main__':
    write_sheet_xls('.\excle操作\表单测试用例V1.0.0版20200628.xls', '.\excle操作\测试用例V1.0.0版20200628.xls')