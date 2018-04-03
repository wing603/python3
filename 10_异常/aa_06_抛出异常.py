def input_password():
    pwd = input("请输入密码：")
    if len(pwd) >= 8:
        return pwd
    # pwd<8抛出异常
    print("主动抛出异常")
    # 创建异常对象
    ex = Exception("密码长度不够")
    # 主动抛出异常
    raise ex


try:
    print(input_password())
except Exception as reslut:
    print(reslut)
