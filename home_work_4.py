from functools import reduce

import my_calc


class HomeWork4:
    def __init__(self):
        self.size = 32
        self.lst = [20, -3, 15, 2, -1, -21]
        self.a = 6
        self.b = 3

    def square(self):
        """4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
        периметр квадрата, площадь квадрата и диагональ квадрата."""
        perimeter = 4 * self.size
        square_area = self.size ** 2
        diagonal = self.size * 2 ** 0.5
        return perimeter, square_area, diagonal

    def get_person_info(self, **info):
        """4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
        в формате аргумент: значение. Например:
                                            name: John
                                            last_name: Smith
                                            age: 35
                                            position: web developer"""
        lst = [f"{key}:{value}" for key, value in info.items()]
        return lst

    def lst_items_greater_zero(self):
        """4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
        положительные числа"""
        return list(filter(lambda x: x > 0, self.lst))

    def multiplying_list_values(self):
        """4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке """
        return reduce(lambda x, y: x * y, self.lst)

    def calc_operations(self, operation):
        """4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
     Примените эти функции в качестве методов в другом файле."""
        if operation == "+":
            return my_calc.sum(self.a, self.b)
        elif operation == "-":
            return my_calc.minus(self.a, self.b)
        elif operation == "*":
            return my_calc.multi(self.a, self.b)
        elif operation == "/":
            return my_calc.division(self.a, self.b)
        else:
            return "Введена неверная математическая операция "


if __name__ == '__main__':
    operations = input("Введите математическую операцию (+, -, *, /): ")
    hw = HomeWork4()
    print(hw.square())
    print(*hw.get_person_info(name='John', last='Smith', a=35, po='web developer'), sep='\n')
    print(hw.lst_items_greater_zero())
    print(hw.multiplying_list_values())
    print(hw.calc_operations(operations))
