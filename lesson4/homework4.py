
from math import sqrt

# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
def square(side):
    return side * 4, side ** 2, side * sqrt(2)

print('*' * 20 + ' Task 4.1 ' + '*' * 20)
side = int(input('Enter side of square: '))
print(square(side))

# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
def printEmployee(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')

print('*' * 20 + ' Task 4.2 ' + '*' * 20)
printEmployee(last_name='Popov', name='Max', age=40, position='web developer')

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
print('*' * 20 + ' Task 4.3 ' + '*' * 20)
my_list = [20, -3, 15, 2, -1, -21]
print(list(filter(lambda x: x > 0, my_list)))

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
from functools import reduce
print(reduce(lambda x, y: x * y, my_list))
# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
print('*' * 20 + ' Task 4.4 ' + '*' * 20)
from my_calc import *

sum_res = sum(100, 20)
print(sum_res)

prod_res = prod(100, 20)
print(prod_res)

div_res1 = divide(45, 9)
print(div_res1)

div_res2 = divide(5, 0)
print(div_res2)

remain_res = remain(541, 6)
print(remain_res)

sub_res = subtract(230, 149)
print(sub_res)


def tests():
    assert sum(5, 8) == 13, f'Wrong number, actual result is {sum(5, 8)}'
    assert prod(10, 6) == 60, f'Wrong number, actual result is {prod(10, 6)}'
    assert divide(10, 0) == "Can't divide by zero", "Shouldn't divide by zero"
    assert subtract(85, 28) == 57,  f'Wrong number, actual result is {subtract(85, 28)}'
    assert remain(9, 4) == 1, f'Wrong number, actual result is {remain(9, 4)}'

tests()

