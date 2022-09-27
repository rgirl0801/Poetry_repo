# # 4.1
# def square(storona_kvadrata):
#    perimetr = 4 * storona_kvadrata
#    ploshad = 2 * storona_kvadrata
#    diagonal = (storona_kvadrata * 2) + (storona_kvadrata * 2)
#    return perimetr, ploshad, diagonal
#
#
# print(square(16))
#
#
# # 4.2
# def stroka(name, last_name, age, position):
#    return f'name: {name} \n last_name: {last_name} \n age: {age} \n position: {position}'
#
#
# print(stroka('John', 'Doe', 35, 'web developer'))
#
# # 4.3
# lst = [1, 3, -4, 5, -100, -2000, 5, 0]
# list_result2 = [x for x in lst if x >= 0]
# list_final = list(filter(lambda x: x >= 0, lst))
# print(f'list without negatives:  {list_final} list with negatives {lst}')
#
# from functools import reduce
#
# # 4.4
# print(f'list:  {list_final} ')
#
# sum = reduce(lambda x, y: x + y, list_final)
# print(sum)
#
# ------------------------------------------------
# from functools import reduce
# from my_calc import *
#
# print('\nTask #4.1')
# print('-' * 10)
#
#
# def square(a):
#    return 4 * a, a * a, round(2 ** (1 / 2) * a, 2)
#
#
# print(square(2))
# print(square(3))
#
# print('\nTask #4.2')
# print('-' * 10)
#
#
# def name_arg(**kwargs):
#    for key, value in kwargs.items():
#        print("{}: {}".format(key, value))
#
#
# name_arg(name='Лев', last_name='Толстой', age=85, position='писатель', book='Война и мир')
#
# print('\nTask #4.3')
# print('-' * 10)
# my_list = [20, -3, 15, 2, -1, -21]
# print(list(filter(lambda x: x > 0, my_list)))
# # или другое решение - без lambda
# print([x for x in my_list if x > 0])
#
# print('\nTask #4.4')
# print('-' * 10)
#
#
# print(reduce(lambda x, y: x * y, my_list))
#
# print('\nTask #4.5')
# print('-' * 10)
#
# print(my_sum(79, 11))
# print(my_sub(-10, 57))
# print(my_mult(34, 17))
# print(my_div(12, 5))
# print(my_div(100, 0))
# print(my_exp(10, 10))
#
#
# --------my_calc.py----------
# def my_sum(x, y):
#    return x+y
#
# def my_sub(x, y):
#    return x-y
#
# def my_mult(x, y):
#    return x*y
#
# def my_exp(x, y):
#    return x**y
#
#
#  def my_div(x, y):
#    try:
#        return x / y
#    except ZeroDivisionError:
#        return("Zero Division Error occurred")
#
#
#
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=[homework4]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# from math import sqrt
# from functools import reduce
# from my_calc import *
#
# def square(square_side: int) -> tuple:
#     return square_side * 4, square_side ** 2, square_side * sqrt(2)
#
# print('-' * 10 + ' Task 4.1 ' + '-' * 10)
# print(square(2))
# print(square(5))
#
# print('-' * 10 + ' Task 4.2 ' + '-' * 10)
#
# def print_args(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {str(value)}')
#
# print_args(name='John', last_name='Smith', age=35, position='web developer')
# print('-' * 10)
# print_args(title='Достучаться до небес', director='Thomas Jahn', year=1997, budget=2200000, main_actor='Til Schweiger',
#            slogan='Быстрый автомобиль, миллион марок в багажнике, и всего одна неделя жить')
#
# print('-' * 10 + ' Task 4.3 ' + '-' * 10)
# my_list = [20, -3, 15, 2, -1, -21]
# print(f'Initial list: {my_list}')
# my_list_pos = list(filter(lambda x: x > 0, my_list))
# print(f'Positive values: {my_list_pos}')
# my_list_mul = reduce(lambda x, y: x * y, my_list)
# print(f'Multiplication result: {my_list_mul}')
#
# print("-" * 10 + " Task 4.4 " + "-" * 10)
# print(f'10+35={sum_(10, 35)}')
# print(f'87-11={sub_(87, 11)}')
# print(f'2*17={mul_(2, 17)}')
# print(f'128/2={div_(128, 2)}')
# print(f'2^10={pow_(2, 10)}')
# print(f'12/0={div_(12, 0)}')
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=my_calc.py-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# def sum_(a, b):
#     return a + b
#
# def sub_(a, b):
#     return a - b
#
# def mul_(a, b):
#     return a * b
#
# def div_(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as ex:
#         return repr(ex)
#
# def pow_(a, b):
#     return a ** b
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=test_hw4.py-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# import pytest
# from my_calc import *
#
# test_cases = ((1, 2), (3, 4), (-1, 4), (3, -10), (10, 0), (0, 6), (-4, 2), (18, -7))
#
# @pytest.mark.parametrize('a, b', test_cases)
# def test_sum_(a, b):
#     assert sum_(a, b) == a + b
#
# @pytest.mark.parametrize('a, b', test_cases)
# def test_sub_(a, b):
#     assert sub_(a, b) == a - b
#
# @pytest.mark.parametrize('a, b', test_cases)
# def test_mul_(a, b):
#     assert mul_(a, b) == a * b
#
# @pytest.mark.parametrize('a, b', test_cases)
# def test_div_(a, b):
#     if b:
#         assert div_(a, b) == a / b
#     else:
#         assert div_(a, b) == "ZeroDivisionError('division by zero')"
#
# @pytest.mark.parametrize('a, b', test_cases)
# def test_pow_(a, b):
#     assert pow_(a, b) == a ** b
# -=-=-=-=-=[/homework4] [https://github.com/AlexTotoro/qa-for-everyone]=-=-=-=-=-