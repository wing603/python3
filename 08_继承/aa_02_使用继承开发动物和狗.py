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
        print("jiao")

xiaoli = Dog()
xiaoli.eat()
xiaoli.run()

class littleDog(Dog):
    def make(self):
        print("make")

l_dog = littleDog
l_dog.run()
l_dog.dark()