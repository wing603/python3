class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, play_name):
        self.play_name = play_name

    @staticmethod
    def show_help():
        print("帮助信息。。。")

    @classmethod
    def show_top_score(cls):
        print("历史分数%d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏" % self.play_name)


# 查看游戏帮助信息
Game.show_help()
# 查看历史最高分
Game.show_top_score()
# 创建游戏对象
game = Game("小明")
game.start_game()
print(game.play_name)
