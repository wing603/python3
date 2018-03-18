has_ticket = True
knife_length = 11
if has_ticket:
    print("可以进安检")
    if knife_length > 20:
        print("刀长，有 %d 公分长" % knife_length)
        print("不允许上车")
    else:
        print("祝您旅途愉快")
else:
    print("不可以进安检")