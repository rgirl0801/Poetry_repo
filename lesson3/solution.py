#3.1.
#Option 1
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])

# Option 2. Using deconstruction
my_list = ['a', 'b', [1, 2, 3], 'd']
list1 = my_list[2]
print(*list1, sep='\n')

#3.2.
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#Using lambda and filter
print(sum(filter(lambda x: isinstance(x, int), list_1)))
#Using list comprehension
print([x for x in list_1 if isinstance(x, str) and 'a' in x])

#3.3.
print(tuple(['cat', 'dog', 'horse', 'cow']))

#3.4.
family_1 = tuple(input('Введите текст через запятую: ').split(','))
family_2 = tuple(input('Введите текст через запятую: ').split(','))
if len(family_1) == len(family_2):
    print('Equal')
elif len(family_1) > len(family_2):
    print('family_1')
else:
    print('family_2')

#3.6.
# Option 1
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
result = 0
for x in my_dictionary:
    result += my_dictionary[x]
print(result)


# Option 2
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))


#3.7.
new_list = set([1, 2, 3, 4, 5, 3, 2, 1])
print(new_list)

#3.8.
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set2.issubset(set1))