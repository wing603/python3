def demo(num,*nums,**person):
    """

    :param num:
    :param nums: *代表元组
    :param person: **代表字典
    """
    print(num)
    print(nums)
    print(person)

demo(1)
demo(1,2,3,4,name="wangjing",age=27)