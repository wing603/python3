def demo(num,num_list):
    print("函数内部代码")
    #num = num + num
    num += num
    #列表变量使用+=不会做相加再赋值的操作
    # num_list += num_list本质上是在调用列表的extend方法
    # num_list += num_list
    num_list.extend(num_list)

    print(num)
    print(num_list)
    print("执行结束")

num1 = 9
num_list1 = [1,2,3]
demo(num1,num_list1)
print(num1)
print(num_list1)