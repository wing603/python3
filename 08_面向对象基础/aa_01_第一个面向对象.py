class Cat():
    def eat(self):
        print("吃鱼")
    def drink(self):
        print("喝水")
# 创建对象
tom = Cat()
tom.drink()
tom.eat()
# 可以看到是那一个类创建的 和内存中的地址
print(tom)
# addr = id(tom)
# print("%d" % addr)