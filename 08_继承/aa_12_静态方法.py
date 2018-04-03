class Dog(object):
    @staticmethod
    def run():
        print("狗跑")
# 通过类名直接调用静态方法
# 不需要创建实例对象
# 不访问实例属性或类属性 可以创建精通方法
Dog.run()