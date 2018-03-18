def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    assert b != 0
    return a / b


if __name__ == "__main__":
    c = add(1, 2)
    print(c)
    d = subtract(2, 1)
    print(d)
    e = multiply(2, 2)
    print(e)
    f = divide(1, 2)
    print(f)
