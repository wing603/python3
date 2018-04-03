import xlrd
import os

file_name = 'D:\\data1.xlsx'

file_path = os.path.join(os.getcwd(),file_name)

text = xlrd.open_workbook(file_path)
"""
单元个批量处理
"""
#读取sheet 1月 信息
t1 = text.sheet_by_name("Sheet1")
#获取第一行所有内容    合并单元格   首行显示值 ，其他为空
print(t1.row_values(0))
#获取单元格值类型和内容
print(t1.row(0))
#获取单元格数据类型
print(t1.row_types(0))