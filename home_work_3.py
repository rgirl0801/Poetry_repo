""""3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3  +

3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   - получите сумму всех чисел, +
   - распечатайте все строки, где есть буква 'a' +

3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж +
3.4. Напишите программу, которая определяет, какая семья больше. +
      1) Программа имеет два input() - например, family_1, family_2.
      2) Членов семьи нужно перечислить через запятую.
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    о вашем любимом фильме.
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение

3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга"""



class HomeWork3:
    def __init__(self, my_list, list_1, lst, my_dictionary, del_duplicate_items,
                 sett1, sett2, family_1, family_2, description_film):

        self.my_list = my_list
        self.list_1 = list_1
        self.lst = lst
        self.family_1 = family_1
        self.family_2 = family_2
        self.description_film = description_film
        self.my_dictionary = my_dictionary
        self.del_duplicate_items = del_duplicate_items
        self.sett1 = sett1
        self.sett2 = sett2

    def print_item_list(self):
        """Метод вывода на экран заданного элемента списка"""
        for item in self.my_list:
            if isinstance(item, list):
                print(*item)
            elif 'a' in item:
                print(item)

    def get_sum_list_item(self):
        """Метод подсчета значений элемента спаиска"""
        return sum(filter(lambda x: isinstance(x, int), self.list_1))

    def list_to_tuple(self):
        """Метод преобразования списка в кортеж"""
        return tuple(self.lst)

    def check_big_family(self):
        """Метод определения бОльшей семьи"""
        print('Family_1' if len(self.family_1) > len(self.family_2) else 'Equal' if len(self.family_1) == len(
            self.family_2) else 'Family_2')

    def create_dict_and_get_data(self):
        """Метод создания словоря film"""
        film = {}
        if len(self.description_film) == 6:
            film['title'] = self.description_film[0]
            film['director'] = self.description_film[1]
            film['year'] = self.description_film[2]
            film['budget'] = self.description_film[3]
            film['main_actor'] = self.description_film[4]
            film['slogan'] = self.description_film[5]
        else:
            print('Введены не все значения описания фильма')
        print(film.keys(), film.values(), film.items(), end='\n')

    def clear_duplicate_items(self):
        """Метод удаления повторяющихся элементов из списка"""
        return list(set(self.del_duplicate_items))

    def get_sum_items_dict(self):
        return sum(self.my_dictionary.values())

    def operations_set(self):
        """Метод проведения операций над множествами"""
        print(
            "Множество sett1 и sett2 являются подмножеством друг друга" if any((self.sett1.issubset(self.sett2),
                                                                                self.sett2.issubset(
                                                                                    self.sett1))) else "Множество sett1 и sett2 не являются подмножеством друг друга")


if __name__ == '__main__':
    my_list = ['a', 'b', [1, 2, 3], 'd']
    list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
    lst = ['cat', 'dog', 'horse', 'cow']
    family_1 = input('Введите через запятую имена членов семьи #1, в конце ввода нажминет Enter:  ').split(',')
    family_2 = input('Введите через запятую имена членов семьи #2, в конце ввода нажминет Enter:  ').split(',')
    description_film = input('Введите описание Вашего фильма. Через запятую укажите: название, режиссер, год выпуска,\
    бюджет, главный актер, слоган. В конце ввода нажминет Enter: ').split(',')
    my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
    del_duplicate_items = [1, 2, 3, 4, 5, 3, 2, 1]
    sett1, sett2 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
    film = {}
    hw = HomeWork3(my_list, list_1, lst, my_dictionary, del_duplicate_items,
                   sett1, sett2, family_1, family_2, description_film)
    print(hw.get_sum_items_dict())
    print(hw.get_sum_list_item())
    print(hw.list_to_tuple())
    print(hw.clear_duplicate_items())
    hw.create_dict_and_get_data()
    hw.check_big_family()
    hw.print_item_list()
    hw.operations_set()
