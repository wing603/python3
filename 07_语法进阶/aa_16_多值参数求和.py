def sum_numbers(*args):
    num = 0
    print(num)
    print(args)
    for n in args:
        num += n
    return num

r = sum_numbers(1,2,3)
print(r)