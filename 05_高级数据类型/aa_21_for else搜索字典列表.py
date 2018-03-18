info_list = [{"name":"王晶"},
             {"name":"小王"}]
find_name = "小"
for info_dict in info_list:
    print(info_dict)
    if info_dict["name"] == find_name:
        print("找到了 %s" %find_name)
        break
else:
    print("没有找到 %s" %find_name)
print("查找结束")