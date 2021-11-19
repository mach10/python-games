def make_factorial(num):
    if type(num) == str:
        raise TypeError
    if num < 0:
        raise TypeError

    return 1