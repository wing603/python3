hello_str = "hello world"

# 1. 判断是否以指定字符开始

print(hello_str.startswith("hel"))
# 2. 判断是否以指定字符串结束
print(hello_str.endswith("ld"))
# 3. 查找指定字符串
# index通用可以查找指定字符串再大字符串种的索引
# find如果指定字符串不存在会返回-1
# index如果指定字符串不存在会报错
print(hello_str.find("llo"))
hello_str.index("132")
# 4. 替换字符串
# replace方法执行完成之后 会返回一个新的字符串
# 注意：！！ 不会修改原有字符串的内容
print(hello_str.replace("world","python"))
print(hello_str)