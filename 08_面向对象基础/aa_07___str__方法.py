class Cat:

    def __init__(self,new_name):

        self.name = new_name
        print("%s来了"% self.name)
    def __del__(self):
        print("%s去了"% self.name)
    def __str__(self):
        # __str__必须返回一个字符串
        # print打印对象变量 想看到自定义的信息
        return "我是小猫"
tom = Cat("Tom")
print(tom)

# del tom
print("111111111")
