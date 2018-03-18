#全局变量
gl_num = 1
gl_title = "小明"

def demo1():
    #局部变量和全局变量名称相同 变量下方有虚线
    num = 99
    print("demo1 ==> %d" % num)
    print("%s" % gl_title)

def demo2():

    print("demo2 ==> %d" %num)

demo1()
demo2()