def print_info(name, title="", gender=True):

    gender_test = "男生"
    if not gender:
        gender_test = "女生"
    print("[%s]%s 是 %s" % (title, name, gender_test))


print_info("老王")
print_info("小妹",gender=False)
