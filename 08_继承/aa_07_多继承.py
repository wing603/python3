class A:
    def test(self):
        print("A")


class B:
    def demo(self):
        print("B")


class C(A, B):
    """
    多继承可以让子类对象
    同时具有多个父类的方法和属性
    """
    pass


c = C()
c.test()
c.demo()
