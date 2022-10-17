import functools


def sum_arrays(*args):
    sum = 0
    for arr in args:
        sum += functools.reduce(lambda a, b: a + b, arr)
    return sum


def sum_arrays2(arr1, arr2):
    return sum(arr1 + arr2)


def sum_arrays3(arr1, arr2):
    return functools.reduce(lambda a, b: a + b, arr1 + arr2)


def average(arr):
    # return float('%.2f' % (sum(arr) / len(arr) if len(arr) > 0 else 0))
    return round(sum(arr) / len(arr) if len(arr) > 0 else 0, 2)
