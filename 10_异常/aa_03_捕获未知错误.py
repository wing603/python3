try:

    num = int(input("请输入数字："))
    res = 8 / num
    print(res)


except ValueError:
    print("错误值为字母")

except Exception as reslut:
    print("未知错误%s" % reslut)