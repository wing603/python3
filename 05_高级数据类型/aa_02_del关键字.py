name_list = ["张三", "李四", "王五"]
# del 删除列表元素
# del 关键字本质是用来讲一个变量从内存中删除
# 建议删除数据使用列表方法
del name_list[1]

name = "小明"
del name
# 使用del关键字奖变量从内存种删除
# 后续代码就不能在使用这个变量

print(name_list)