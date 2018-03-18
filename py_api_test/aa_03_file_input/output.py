# r = open("D:/MyDrivers/file2.txt","r")
# # file = r.read()
# # print(file)
# # r.close()
# r = open("D:/MyDrivers/file2.txt","w")
# r.write("hello world")
# r.close()
# r = open("D:/MyDrivers/file2.txt","r")
# r = r.read()
# print(r)


class A(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return A
a=A('hello')
print(a.name)
print(a.getName())