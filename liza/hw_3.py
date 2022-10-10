print('\n     #  3.1')
my_list = ['a', 'b', [1, 2, 3], 'd']

print(*my_list[2], sep=", ")

print('\n     #  3.2')
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
list_2 = [x for x in list_1 if isinstance(x, int)]
print(sum(list_2))

print('\n     #  3.3')
list_3 = ['cat', 'dog', 'horse', 'cow']
list_3 = tuple(list_3)
print(list_3)

print('\n     #  3.4')
def compare_families():
    f1 = input("Please, enter first family: ")
    f2 = input("Please, enter second family: ")
    print( f1 if len(f1) > len(f2) else f2 if len(f1) < len(f2) else "Equal")


# compare_families()

print('\n     #  3.5')
film = {
    'title': 'Jesus Christ Superstar',
    'director': 'Norman Jewison',
    'year': 1973,
    'budget': '$3.5 million',
    'main_actor': 'Ted Neeley',
    'slogan': 'People who are hungry, people who are starving, they matter more than your feet and hair!'
}

k = list(film.keys())
print(k)

v = list(film.values())
print(v)

print(film, '\n')
i = film.items()
print(*i, sep='\n')

print('\n     #  3.6')
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
sum_ = 0
for key in my_dictionary:
    sum_ += int(my_dictionary[key])

print(sum_)

print('\n     #  3.7')

arr = [1, 2, 3, 4, 5, 3, 2, 1]
arr = list(set(arr))
print(arr)

print('\n     #  3.8')

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

set_intersect = set1.intersection(set2)
print(set_intersect)

set_diff_1 = set1.difference(set2)
set_diff_2 = set2.difference(set1)
print(set_diff_1, set_diff_2)
print(set1.symmetric_difference(set2))

is_subset = set1.issubset(set2) or set2.issubset(set1)
print(is_subset)

print('\n =============')

print(235, 'jyg', 659, sep=', ')