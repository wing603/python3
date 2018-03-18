import random

player= int(input("请输入你要出的拳 石头1，剪刀2，布3:"))

computer = random.randint(1,3)

print("玩家选择的拳头是 %d - 电脑出的拳头是 %d" % (player,computer))

if ((player == 1 and computer ==2)
    or (player ==2 and computer== 3)
    or (player ==3 and computer==1)):
    print("玩家胜利")
elif player == computer:
    print("平局")
else:
    print("电脑胜利")