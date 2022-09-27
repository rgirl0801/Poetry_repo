def move(position, roll):
    return position + 2 * roll


def past(h, m, s):
    return (3600 * h + 60 * m + s) * 1000


def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1


def century(year):
    return (year + 99) // 100


def check_for_factor(base, factor):
    return base % factor == 0


def fibonacci(n: int) -> int:
    arr = [0, 1]
    i = 2
    while i <= n:
        arr.append(arr[i - 1] + arr[i - 2])
        i += 1
    return arr[n]


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))


def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    x, y = 0, 1
    for i in range(n):
        x, y = y, y + x
    return x
