class Tools(object):
    # 定义类属性
    count = 0

    def __init__(self, name):
        self.name = name
        Tools.count += 1


tool1 = Tools("榔头")
tool2 = Tools("斧头")
tool3 = Tools("水桶")

print(Tools.count)
