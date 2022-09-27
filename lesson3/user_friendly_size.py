# Написать функцию user_friendly_size, которая принимает размер файла в байтах.
# Функция должна возвращать float (2 decimal precision) в User Friendly Size (Kb, Mb, Gb, Tb, Pb, Eb, Zb, Yb)
# Using tests up to you (pytest or just print)
# challenge: pass the file path the fn and fn should return the size of the file

# for example:
# user_friendly_size(9999) -> 9.76 Kb
# user_friendly_size(9999999) -> 9.54 Mb
import os
import math

def user_friendly_size(size):
    symbols = ('B', 'kB', 'MB', 'GB', 'TB')
    if isinstance(size, str):  # Если аргумент - строка
        if size.isdigit():  # Если протупили и отправили число строкой
            size = int(size)
        else:
            size = os.stat(size).st_size  # Получим размер файла в байтах
    sym_index = int(math.log(size, 2) // 10)
    return f'{size / 2 ** (sym_index * 10):.2f} {symbols[sym_index]}'

print(user_friendly_size(9999)) # 9.76 Kb
print(user_friendly_size(9999999)) # 9.54 Mb