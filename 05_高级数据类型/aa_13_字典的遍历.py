wangjing_dict = {"name": "王晶",
                 "age": 23,
                 "sex": True}
# 遍历字典
# wangjing_info每一次遍历获取到的键值对的key
for wangjing_info in wangjing_dict:

    print("%s-%s" % (wangjing_info,wangjing_dict[wangjing_info]))