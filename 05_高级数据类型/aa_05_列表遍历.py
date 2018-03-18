name_list = ["zhangsan", "lisi", "wangwu"]

"""
顺序的从列表中获取数据，每一次循环过程中，
数据都会保存在iname这个变量种，再循环体内部
可以访问到当前这一次获取到的数据
for 变量名 in 列表名:

    print("我的名字是： %s " % iname)

"""
for iname in name_list:

    print("我的名字是： %s " % iname)
    print(iname)