def test(num):
    print("在函数内部%d对应的内存地址是%d" % (num,id(num)))
    # 定义一个字符串变量
    result = "Hello"
    print("%s字符串返回的内存地址是%d" %(result,id(result)))
    # 返回字符串变量地址
    return result
# 1.定义一个数字变量
a = 1
# 数据的地址本质就是一个数字
print("a变量的内存地址是 %d" % id(a))

# 2.调用函数test 本质上传递的是实参保存数据的引用
# 如果函数有返回值 但没有定义变量接受
# 程序不会报错 但是无法获取返回结果

r = test(a)
print("%s的内存地址是%d " %(r,id(r)))


