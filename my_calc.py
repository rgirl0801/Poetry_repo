def sum(a, b):
    if not all(map(lambda x: isinstance(x,(int, float)),(a,b))):
        raise TypeError("Аргументы a и b должны быть целыми или вещественными числами")
    return a + b


def minus(a, b):
    if not all(map(lambda x: isinstance(x,(int, float)),(a,b))):
        raise TypeError("Аргументы a и b должны быть целыми или вещественными числами")
    return a - b


def multi(a, b):
    if not all(map(lambda x: isinstance(x,(int, float)),(a,b))):
        raise TypeError("Аргументы a и b должны быть целыми или вещественными числами")
    return a * b


def division(a, b):
    if not all(map(lambda x: isinstance(x,(int, float)),(a,b))):
        raise TypeError("Аргументы a и b должны быть целыми или вещественными числами")
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Делить число на 0 нельзя')


