from functools import reduce

print('\n______ # 1 _______')

def square(a):
    return (4 * a, a * a, 2 ** (1/2) * a)

print(square(4))
print(square(0))
print(square(10))

print('\n______ # 2 _______')

def print_arg(**kwargs):
    my_dict = {}
    for key in kwargs:
        print(key, kwargs[key], sep=': ')
        my_dict[key] = kwargs[key]
    return my_dict

print(print_arg(name = 'John',
    last_name = 'Smith',
    age = 35,
    position = 'web developer'))


print('\n______ # 3 _______')

my_list = [20, -3, 15, 2, -1, -21]
new_list = list(filter(lambda x: x > 0, my_list))

print(new_list)

print('\n______ # 4 _______')

mult = reduce(lambda x, mult: mult * x, new_list, 1)
print(mult)

print('\n______ # 5 _______')

import my_calc

print(my_calc.summa(56, -589))
print(my_calc.diff(68, -986))
print(my_calc.mult(69, 81))
print(my_calc.div(57, 5))
print(my_calc.div(57, 0))
