info_tuple = ("zhangsan", 12,1.11,12)

# 1.取值和取索引
print(info_tuple[3])

print(info_tuple.index(12))
# 统计计数
print("12出现的次数是 %d" %info_tuple.count(12))
# 统计元组中元素个总数
# print(len(info_tuple))
s_len = len(info_tuple)
print(s_len)