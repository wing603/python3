#全局变量
num = 1
title = "小明"

def demo1():
    # 希望修改全局变量的值
    # global 声明一下变量
    # 在使用赋值语句时，就不会创建局部变量
    global num
    num = 99
    print("demo1 ==> %d" % num)
    print("%s" % title)

def demo2():

    print("demo2 ==> %d" %num)

demo1()
demo2()