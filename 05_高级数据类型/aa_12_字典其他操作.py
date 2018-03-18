wangjing_dict = {"name": "王晶",
                 "age": 23}
# 1.统计字典键值对数量
print(len(wangjing_dict))
# 2.合并字典 如果存在被合并的字典中包含已经存在的键值对会
#覆盖之前的键值对
temp_dict = {"sex":True,
             "weight":62}
wangjing_dict.update(temp_dict)
# 3.清空字典
wangjing_dict.clear()


print(wangjing_dict)