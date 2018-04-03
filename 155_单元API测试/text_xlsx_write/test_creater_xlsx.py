import xlsxwriter
import os
import datetime
#创建文件
workbook = xlsxwriter.Workbook("data2.xlsx")
#创建sheet
worksheet = workbook.add_worksheet("num1")
#写入数字和文本
worksheet.write('A1',"123")
worksheet.write(3,4,"234")     #索引行为2 列为2 内容234
worksheet.write("A2","Hello world")
#写入函数
# worksheet.write(1,2,"=sum(B1:B2)")
#写入图片
worksheet.insert_image(0,5,"1233.jpeg")
worksheet.insert_image(0,5,"1233.jpeg",
                       {"url":"http://httpbin.org/"})
#写入时间
d = workbook.add_format({'num_format': 'yyyy-mm-dd'})
worksheet.write(3,3,datetime.datetime.strptime('2018-03-27',
                                               '%Y-%m-%d'),d)
#设置行属性
worksheet.set_row(0,30)
#设置列属性
worksheet.set_column("C:D",20)
# 自定义格式
f = workbook.add_format({'border': 1, 'font_size': 13, 'bold': True, 'align': 'center','bg_color': 'cccccc'})
worksheet.write('A3', "python excel", f)
worksheet.set_row(0, 40, f)
worksheet.set_column('A:E', 20, f)
#批量单元格写入
worksheet.write_column("A15",[1,2,3,4,5,6,7,8])
worksheet.write_row("B3",[11,22,33,44,55,66])

# 合并单元格写入
worksheet.merge_range(7,5, 11, 8, 'merge_range')

#关闭文件
workbook.close()
