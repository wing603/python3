def demo():
    return int(input("请输入整数："))


def demo1():
    return demo()


# 利用异常的传递性 再主程序捕获异常
try:
    print(demo1())
except Exception as result:
    print("未知错误%s" % result)
