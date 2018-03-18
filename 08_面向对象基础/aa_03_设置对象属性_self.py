class Cat:
    def eat(self):
        print("%s 猫1" %self.name)
    def drink(self):
        print("猫2")
# 创建对象
tom = Cat()
# 可以使用 .属性名利用赋值语句就可以
tom.name = "tom"
tom.eat()
tom.drink()

tom1 = Cat()
tom1.name = "tom1"
tom1.eat()
tom1.drink()

print(tom)
print(tom1)
