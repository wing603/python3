# 参数a代表追加内容append

f = open("README", "a")

# 参数w代表追加内容write

# f = open("README", "w")
"""
r+：读写
w+：读写  覆盖
a+：读写  指针放在文件结尾

"""


w = f.write("1234")

print(w)
f.close()
