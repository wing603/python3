def sum_numbers(num):

    print(num)
    # 递归的出口 当参数满足某个条件时 不再执行函数
    # 不判断会出现死循环
    if num == 1:
        return
    #自己调用自己
    sum_numbers(num - 1)

sum_numbers(3)