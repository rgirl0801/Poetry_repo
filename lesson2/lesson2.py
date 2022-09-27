# Booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
print(bool(["apple", "cherry", "banana"]))

# False values:
print(bool(False))
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))

# Python Operators
print(10 + 5)

# Python If ... Else
a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

a = 33
b = 200

if b > a:
  pass

# Python While Loops
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass

# Python Functions
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

def my_function():
  print("Hello from a function")

my_function()

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction():
  pass

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# Проверяем возраст посетителя и в зависимости от вводных данных решаем, может ли он посетить заведение
age = float(input('Enter your age: '))
if age < 13:
    print("Where's your mom?")
elif age >= 21:
    print('Welcome!')
else:
    print('Go home')

# Обратный отчет с использованием цикла while
i = 5
while i > 0:
    print(i, 'Hello')
    i = i - 1
print('Go!')

# Использование цикла while с оператором continue
i = 0
while i < 5:
    i = i + 1
    if i == 3:
        continue
    print(i)


# Функция для возведения заданного числа в заданную степень
def give_me_power(num, n):
    return num ** n


print(give_me_power(2, 5))
print(give_me_power(2, 4))

# Пример использования условных операторов
x = 2
if x == 5:
    print('Five')
elif x > 5:
    print('More than five')
else:
    print('Less than five')

# Посимвольный вывод введенного слова
name = input('Input your name: ')
for letter in name:
    print(letter)

# Посимвольный вывод введенного слова с указанием индекса символа
name = input('Enter your name: ')
for symbol in name:
    print(f'index {name.index(symbol)} - {symbol}')

# Пример использования выражений, которые приравниваются к булевым (True/False)
number = 0
if name:
    print('true')
else:
    print('false')

#     Использование for цикла в заданном диапазоне range
for i in range(5):
    print(i, 'Hello!')

#     Использование for цикла в заданном диапазоне range с указанием начала, конца и шага (start, stop, end)
for i in range(0, -10, -1):
    print(i)

# Использование for цикла в заданном диапазоне c оператором break

for i in range(5):
    if i == 3:
        break
    print(i)

"""Данная программа, проверяет является ли введенная буква гласной. Здесь в else используется вложенное условие -
  если утверждение во внешнем if - ложное, программа перейдет к else  и начнет проверять вложенное if, если 
  оно также ложно, выполнится команда во вложенном else
  Этот пример мы не рассмотрели на уроке, но вы можете сами поиграть с кодом и проверить, 
  что произойдет, если вы вместо letter.isdigit() поставите letter.isalpha(). Или, что будет, если вы введете сразу 2 символа, 
  или буквы в верхнем регистре? Как насчет специальных символов? Какие изменения нужно будет внести в код, чтобы он работал, как нужно?"""

letter = input()
vowels = 'ioaue'
if letter.isdigit():
    print('It is not a letter')
else:
    if letter in vowels:
        print('vowel')
    else:
        print('consonant')


# Функция с именованными и позиционными аргументами

def person(age, name='Nancy', last_name='Smith'):
    return f'Hello, my name is {name} {last_name}. I am {age} years old'


print(person(18, last_name='Pavlova', name='Anna'))