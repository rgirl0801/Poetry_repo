nums = int(input('Введите число байт: '))
item = input('Введите единицу измерения (Kb, Mb, Gb, Tb): ').lower()


def convert(data, item):
    if item == "kb":
        return round(data / 2 ** 10, 2)
    elif item == 'mb':
        return round(data / 2 ** 20, 2)
    elif item == 'gb':
        return round(data / 2 ** 30, 2)
    elif item == 'tb':
        return round(data / 2 ** 40, 2)


print(f'{convert(nums, item)} {item}')
