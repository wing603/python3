name_list = ["zhangsan", "lisi", "wangwu"]
# 1.取值取索引

print(name_list[1])
# 知道数据内容 想确定所在的位置
print(name_list.index("lisi"))
# 2.修改列表数据
name_list[1] = "李四"
# 3.增加列表数据
# append 可以再末尾增加数据
name_list.append("wangxiaoer")
# inster 可以再列表的指定索引位置插入数据
name_list.insert(1,"liuyi")
# extend 可以吧另外列表全部数据追加到当前列表的末尾
temp_list = ["songwukong", "zhuerge", "shashidi"]
name_list.extend(temp_list)
# 4.删除
# remove 可以从列表种删除指定数据
name_list.remove("wangwu")
# pop 默认可以把列表种最后一个元素删除
name_list.pop()
# pop 也可以指定要删除元素的索引 删除指定索引位置的数据
name_list.pop(3)
# clear 可以清空列表所有数据
name_list.clear()

print(name_list)