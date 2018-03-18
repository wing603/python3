def demo(*args,**kwargs):

    print(args)
    print(kwargs)
# 元组变量 字典变量
info_tuple = (1,2,3)
info_dict = {"name":"xiaoming","age":18}
# 拆包 简化元组变量 字典变量的传递
demo(*info_tuple,**info_dict)