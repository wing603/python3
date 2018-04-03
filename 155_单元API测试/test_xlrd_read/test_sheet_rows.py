import xlrd
import os
from datetime import date, datetime

file_name = 'D:\\data1.xlsx'

file_path = os.path.join(os.getcwd(),file_name)

print(file_path)
#打开文件
text = xlrd.open_workbook(file_path)
#获取1月sheet数据汇总
sheet1 = text.sheet_by_name("1月")
#获取sheet1名字
print(sheet1.name)
#获取行
print(sheet1.nrows)
#获取列
print(sheet1.ncols)

