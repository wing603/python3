import xlrd
import os

file_name = 'D:\\data1.xlsx'

file_path = os.path.join(os.getcwd(),file_name)

text = xlrd.open_workbook(file_path)

t1 = text.sheet_by_name("Sheet1")

#转换  第0行第0列转换为A1
print(xlrd.cellname(0,0))
print(xlrd.cellnameabs(0,0))
print(xlrd.colname(30))