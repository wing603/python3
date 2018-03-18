# 列表记录所有的名片字典
card_list = []

def show_menu():
    #显示菜单
    print("*" * 50)
    print("欢迎使用名片管理系统\n")
    print("1.新建名片\t")
    print("2.显示全部\t")
    print("3.查询名片\n")
    print("0.退出系统")
    print("*" * 50)

def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    # 提示用户输入名片信息
    name_str = input("请输入姓名 ：")
    phone_str = input("请输入电话 ：")
    qq_str = input("请输入qq ：")
    email_str = input("请输入邮箱 ：")
    # 使用用户信息建立名片字典
    card_dict = {"name":name_str,
                 "phone":phone_str,
                 "qq":qq_str,
                 "email":email_str}
    # 将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    # 提示用户添加成功
    print("添加 %s 成功" % name_str)
def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")
    # 判断是否存在名片 如果没有 提示用户返回
    if len(card_list) == 0:
        print("当前没有任何的名片记录，请使用新增功能添加名片")
        # 可以返回一个函数的执行结果
        # return 下方的代码不会被执行
        return
    # 打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t\t")
    print("")
    # 打印分割线
    print("=" * 50)
    # 遍历名片依次显示名片信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" %(card_dict["name"],
                                           card_dict["phone"],
                                           card_dict["qq"],
                                           card_dict["email"]))
def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    # 提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名 ：")
    # 遍历card_list查询搜索到的姓名
    # 如果没有找到，返回抱歉没有找到
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("找到 %s" % find_name)
            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("没有找到%s " %find_name)
# 修改删除名片
def deal_card(card_info):
    """处理查找到的名片

    :param card_info:查找到的名片
    """
    print(card_info)
    action_str = input("请选择要执行的操作 "
                       "[1]修改 [2]删除 [0]返回主菜单")
    if action_str == "1":
        card_info["name"] = input_card_info(card_info["name"],"姓名（回车不修改）：")
        card_info["phone"] = input_card_info(card_info["phone"],"电话（回车不修改）：")
        card_info["qq"] = input_card_info(card_info["qq"],"QQ  （回车不修改）：")
        card_info["email"] = input_card_info(card_info["email"],"邮箱（回车不修改）：")
        print("修改名片成功")
    elif action_str == "2":
        card_list.remove(card_info)
        print("删除名片成功")

def input_card_info(dict_value,tip_message):

    """输入名片信息

    :param dict_value:字典中原有的键值
    :param tip_message:输入的提示文字
    :return:如果用户输入内容返回内容；没有输入返回原有的值
    """
    # 1. 提示用户输入内容

    result_str = input(tip_message)

    # 2. 判断用户是否输入内容 用户输入内容 直接返回结果

    if len(result_str) > 0:

        return result_str

    # 3. 用户没有输入内容 返回字典原有的键值

    else:

        return dict_value


