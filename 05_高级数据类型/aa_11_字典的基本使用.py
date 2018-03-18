wangjing_dict = {"name": "王晶",
                 "age": 23,
                 "sex": True,
                 "height": 1.75,
                 "weight": "62kg"}
# 1.字典取值 对应键值key
print(wangjing_dict["name"])

# 2.增加 key不存在 会增加新的键值对
wangjing_dict["hobit"] = "play"

# 修改 key存在 会修改已存在的键值对
wangjing_dict["name"] = "王晶123"

# 3.删除 删除指定键值对 如果指定的键值对不存在程序会报错
wangjing_dict.pop("hobit")

print(wangjing_dict)