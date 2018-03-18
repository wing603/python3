class Cat:
    def __init__(self,new_name):

        print("初始化方法")
        self.name = new_name
        # self.属性 = 形参
        # self.name = "tom"
# 使用类名创建对象 会直接调用__init__初始化方法
# 创建的tom对象可以调用类中的方法
tom = Cat("tom")
tom1 = Cat("tom1")
print(tom.name)
print(tom1.name)


