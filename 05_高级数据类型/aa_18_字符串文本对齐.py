# 顺序并且居中对其输出以下内容

peom = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for peom_str in peom:
    # print(peom_str)
    # 左对齐
    # print(peom_str.ljust(10, " "))
    # 右对齐
    # print(peom_str.rjust(10, " "))
    # 居中
    print(peom_str.center(10," "))