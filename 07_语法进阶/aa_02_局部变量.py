def demo():
    # 定义一个局部变量
    # 创建：执行下方的代码之后才会被创建
    # 系统回收：函数执行完成之后
    num = 1
    print("%d" % num)


def demo1():
    num = "xiaoming"
    print("%s" % num)


demo()
demo1()