class A:
    def test(self):
        print("A--- test方法")

    def demo(self):
        print("A--- demo方法")


class B:
    def test(self):
        print("B--- test方法")

    def demo(self):
        print("B--- demo方法")


class C(A, B):
    """
    多继承可以让子类对象
    同时具有多个父类的方法和属性
    """
    pass


c = C()
c.test()
c.demo()
