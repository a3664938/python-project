# coding:utf-8
import xlrd
from xlutils.copy import copy
class OperationExcel:
    def __init__(self,file_path='../data/interface.xls',sheet_id=0):
        self.file_path=file_path
        self.sheet_id=sheet_id

    # 读取excel中的某个sheet
    def read_excel(self):
        data=xlrd.open_workbook(self.file_path)
        table=data.sheet_by_index(self.sheet_id)
        return table

    # 获取sheet中数据的行数
    def get_lines(self):
        lines=self.read_excel().nrows
        return lines

    # 根据行列id获取sheet中某个单元格数据
    def get_cell_value(self,row,col):
        cell_value=self.read_excel().cell_value(row,col)
        return cell_value

    # 回写excel
    def write_excel(self,row,col,value):
        read_data=xlrd.open_workbook(self.file_path)
        write_data=copy(read_data)
        sheet_data=write_data.get_sheet(self.sheet_id)
        sheet_data.write(row,col,value)
        write_data.save(self.file_path)

    # 根据依赖case_id获取依赖case所在的行
    def depand_row(self,case_id):
        num=0
        for i in self.get_value_by_col():
            if i == case_id:
                return num
            else:
                num=num+1

    # 根据col获取某列所有的值
    def get_value_by_col(self,col=0):
        values_col=self.read_excel().col_values(col)
        return values_col



