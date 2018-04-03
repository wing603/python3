f = open("README")

# readline方法可以分行读取文件

while True:

    t1 = f.readline()

    print(t1)
    if not t1:
        break

f.close()
