from pprint import pprint # для красивого вывода словаря
person = {}
s = 'IVANOV IVAN 19 Samara SGU 4 5 5 5 4 3 5 3'

s = s.split()
print(s)
print('-'*15)
person['last_name'] = s[0]
person['first_name'] = s[1]
person['age'] = int(s[2])
person['city'] = s[3]
person['university'] = s[4]

print(person)
print('-'*15)

person['marks'] = []
for i in s[5:]:
    person['marks'].append(int(i))

pprint(person)

sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}
sweet['weight'] = '230'
sweet['have_topping'] = True
sweet['name'] = 'SuperCake'
sweet['calories'] = 350
print(sweet)