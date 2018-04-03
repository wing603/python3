import xlrd
import os

file_name = 'D:\\data1.xlsx'

file_path = os.path.join(os.getcwd(),file_name)

text = xlrd.open_workbook(file_path)

t1 = text.sheet_by_name("Sheet1")
#获取第1行第2列的值
print(t1.cell_value(1,2))
print(t1.cell(1,2).value)
print(t1.row(1)[2].value)
