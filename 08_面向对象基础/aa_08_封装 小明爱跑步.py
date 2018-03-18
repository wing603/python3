# person
# name,weight
# __init__,__str__,run,eat
class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print("%s体重%.2f公斤" % (self.name, self.weight))

    def __str__(self):

        return "小明"

    def run(self):
        self.weight -=0.5
        print("%s每次跑步会减肥%.2f公斤"% (self.name,self.weight))
        pass

    def eat(self):
        self.weight += 1
        print("%s每次吃东西会增加%.2f公斤"% (self.name,self.weight))
        pass


xiaoming = Person("小明",75)
print(xiaoming)
xiaoming.run()
xiaoming.eat()
