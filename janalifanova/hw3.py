# 3.1 Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print( my_list[2])

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# sum = 0;
# for i in list_1:
#     if type(i) == int:
#         sum +=i
# print(sum)

#    - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# for string in list_1:
#     if type(string) == str:
#         if string.find("a") != -1:
#             print(string)


# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
# l1 = ['cat', 'dog', 'horse', 'cow']
# l2 = tuple(l1)
# print(l2)
# print(type(l2))



# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
#
# family1 = input("enter names using coma \n").split(",")
# family2 = input("enter names using coma \n").split(",")
# print(len(family1)>len(family2))


# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
#
# film ={
#     "title" : "Matrix",
#     "director": "Wachovski",
#     "year" : 1999,
#     "budget" : 63000000,
#     "main actor": "keanu Rivers",
#     "slogan": "Free your mind"
# }
# print(film.values())
# print(film.keys())
# print(film.items())


# # 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dict = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dict.values()))


# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# l1= [1, 2, 3, 4, 5, 3, 2, 1]
# print(list(set(l1)))


# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# print(set2.issubset(set1))
