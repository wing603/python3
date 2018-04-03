class A():
    def __init__(self):
        self.num = 1
        self.__num2 = 100

        print("我是A")

    def __test(self):
        print("私有方法%d %d" % (self.num, self.__num2))

    def test1(self):
        print("公有方法%d"%self.__num2)
        # print("%d" % self.num)
        self.__test()

class B(A):

    def demo(self):
        print("访问父类私有属性%d" % self.__num2)
        self.__test()
        self.test1()


b = B()
# 外界不能直接访问对象的私有属性/和调用私有方法
print(b)
b.test1()
