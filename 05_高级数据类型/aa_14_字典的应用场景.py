# 使用多个键值对 存储描述一个物体的相关信息
# 将多个字典放在一个列表中 再进行遍历
card_list = [{"name":"张三",
              "age":18,
              "phone":12345,
              "qq":111111},
             {"name":"李四",
              "age":22,
              "phone":110,
              "qq":123111}]


for card_info in card_list:
    print(card_info)