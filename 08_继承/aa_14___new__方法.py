class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        # 创建对象时，new会自动被调用
        print("创建对象，分配空间")
        # 为对象分配空间
        s = super().__new__(cls)
        # 返回对象引用
        return s

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()

print(player)
