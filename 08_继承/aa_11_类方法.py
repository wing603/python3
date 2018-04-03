class Tools(object):
    # 定义类属性
    count = 0

    @classmethod
    def Tool_count(cls):
        print("%d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tools.count += 1


tool1 = Tools("榔头")
tool2 = Tools("斧头")
tool3 = Tools("水桶")
Tools.Tool_count()
# print(Tools.count)
