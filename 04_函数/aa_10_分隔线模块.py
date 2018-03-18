def print_line(char,time):

    """打印单行分割线

    :param char: 分割字符
    :param time: 重复次数
    """
    print(char * time)

def print_lines(char,time):

    """打印多行分割线
    :param char: 分割线使用的分割字符
    :param time: 分割线重复的次数
    """
    row = 0
    while row <5:
        print_line(char,time)
        row += 1


name = "黑马程序员"