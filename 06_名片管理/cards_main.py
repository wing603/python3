#！ usr/bin/python3

import cards_tools

# 无限循环
# 用户主动决定什么时候退出循环
while True:
    # TODO 显示功能菜单
    cards_tools.show_menu()
    action_str = input("请输入数字：")
    print("输入的数字是 %s" %action_str)
    if action_str in ["1","2","3"]:
        # 1.新增名片
        if action_str == "1":   #注意action是字符串，不是整型
            cards_tools.new_card()
        # 2.显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 3.查询名片
        elif action_str == "3":
            cards_tools.search_card()
        # pass相当于占位符 保证代码结构正确
        # 程序运行pass不会执行任何操作
        # pass
    elif action_str == "0":
        print("欢迎下次使用")
        break
        # pass
    # 输入其他内容
    else:
        print("输入错误请重新输入")



