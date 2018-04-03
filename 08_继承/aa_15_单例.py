class MusicPlayer(object):

    instance = None

    def __new__(cls, *args, **kwargs):
        #判断类属性是否是空对象
        if cls.instance is None:

            # 调用父类方法 为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回类属性保存的对象引用
        return cls.instance

player = MusicPlayer()
player1 = MusicPlayer()
print(player)
print(player1)