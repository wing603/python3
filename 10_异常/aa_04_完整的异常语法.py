try:

    num = int(input("请输入数字："))
    res = 8 / num
    print(res)


except ValueError:
    print("错误值为字母")

except Exception as reslut:
    print("未知错误%s" % reslut)
# 出现错误不会执行 不出现错误才会执行
else:
    print("尝试成功")
#有无错误都会执行
finally:
    print("都会执行")
print("_" * 50)
