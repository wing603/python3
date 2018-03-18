def sum_numbers(num):

    if num ==1:
        return 1
    temp = sum_numbers(num - 1)
    return num + temp

# r = sum_numbers(1)
# print(r)
print(sum_numbers(4))