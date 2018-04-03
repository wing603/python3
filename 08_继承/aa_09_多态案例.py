class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s玩" % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s飞天玩" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s和%s玩" % (self.name, dog.name))
        dog.game()


# wangcai = Dog("旺财")
wangcai = XiaoTianDog("哮天犬")
xiaoming = Person("小明")

xiaoming.game_with_dog(wangcai)
