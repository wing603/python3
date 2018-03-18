name_list = ["张三", "李四", "王五", "张三"]

# len 函数可以统计列表中元素的总数

list_len = len(name_list)
# count 方法可以统计列表种某一个元素出现的次数
count = name_list.count("张三")

print("列表包含的元素的总数是 %d" % list_len)
print("张三出现了 %d次" % count)
# 列表删除数据 多个重复 删除第一个
name_list.remove("张三")

print(name_list)