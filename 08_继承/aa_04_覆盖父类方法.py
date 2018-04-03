class Animal:
    def eat(self):
        print("chi---")

    def drink(self):
        print("he")

    def run(self):
        print("pao---")

    def sleep(self):
        print("shui")

class Dog(Animal):

    def dark(self):
        print("汪汪叫")

class littleDog(Dog):
    def fly(self):
        print("我会飞")
    def dark(self):
        print("叫的跟神一样")
l_dog = littleDog()
l_dog.fly()
# 如果子类中重写了父类的方法
# 再使用子类对象调用方法时会调用子类重写的方法
l_dog.dark()