

import xlrd
import os

file_name= 'D:\\data1.xlsx'

file_path = os.path.join(os.getcwd(),file_name)

print(file_path)

text = xlrd.open_workbook(file_path)
# 获取所有sheet的名字
print("sheet_names",text.sheet_names())
# 获取所有sheet的数量
print("sheet_num",text.nsheets)
# 获取所有sheet对象 显示对象内存地址
print("sheet_object",text.sheets())
# 通过sheet名查找 显示对象内存地址
print("By_name",text.sheet_by_name("1月"))
# 通过索引查找 显示对象内存地址
print("By_index",text.sheet_by_index(1))