try:

    num = int(input("请输入数字："))
    res = 8 / num
    print(res)

except ZeroDivisionError:
    print("错误值为0")

except ValueError:
    print("错误值为字母")