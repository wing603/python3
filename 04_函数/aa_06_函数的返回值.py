def sum_2_num(num1,num2):
    """对两个数字的求和"""

    result =num1 + num2

    #使用返回值告诉调用者结果
    return result
    #return表示返回下方的代码不能被执行
sum_result = sum_2_num(1,2)
print("计算的结果是 %d" % sum_result)
