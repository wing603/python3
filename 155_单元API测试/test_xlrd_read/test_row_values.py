import xlrd
import os

file_name = 'D:\\data1.xlsx'

file_path =os.path.join(os.getcwd(),file_name)

text = xlrd.open_workbook(file_path)
t1 = text.sheet_by_name("Sheet1")
# 获取第1行索引为2-----索引为5（不包括5）的值
print(t1.row_values(0,2,5))
#获取第1列索引为0-----索引为4（不包括4）的值
print(t1.col_values(0,0,4))
"""
获取索引行 列数索引为5的值
print(t1.row(2))
"""
print(t1.row_slice(2,0,5))
#获取单元格元素的数据类型
print(t1.row_types(2,0,2))
