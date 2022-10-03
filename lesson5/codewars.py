a = "code"
b = "wa.rs"
name = a + b

print(name)

def hello(name):
    # Insert your code below.
    # Don't forget to use `return`.
		return "Hello, " + name

print(hello("John"))

def greet(name):
    #Good Luck (like you need it)
    return "Hello, " + name + " how are you doing today?"

print(greet("John"))

def number_to_string(num):
    # Return a string of the number here!
		return str(num)

print(number_to_string(67))

def string_to_number(s):
    # your code here
    return int(s)

print(string_to_number("1234"))

def get_sum_of_digits(num):
	sum1 = 0
	str1 = str(num)
	for i in str1:
		sum1 += int(i)
	return sum1

print(get_sum_of_digits(1234))

def make_upper_case(s):
    # Code here
		return s.upper()

print(make_upper_case("hello"))

def switcheroo(s):
    #your code here
		return s.replace("a", "1").replace("b", "a").replace("1", "b")

print(switcheroo("abc"))
print(switcheroo("aaabcccbaaa"))

def solve(s):
	countUpper = 0
	countLower = 0
	for i in s:
		if i.isupper():
			countUpper += 1
		else:
			countLower += 1
	if countUpper > countLower:
		return s.upper()
	else:
		return s.lower()

print(solve("code"))
print(solve("CODe"))
print(solve("COde"))

def solution(string):
    return string[::-1]

print(solution("world"))

def is_triangle(a, b, c):
  return True if a + b > c and a + c > b and b + c > a else False

print(is_triangle(1, 2, 2))

def is_lucky(n):
  return n % 9 == 0

print(is_lucky(1230))

def sale_hotdogs(n):
	if n < 5:
		return n * 100
	elif n >= 5 and n < 10:
		return n * 95
	else:
		return n * 90

print(sale_hotdogs(1))
print(sale_hotdogs(5))

def calculator(a,b,sign):
	if not isinstance(a, int) or not isinstance(b, int):
		return 'unknown value'
	match sign:
		case "+":
			return a + b
		case "-":
			return a - b
		case "*":
			return a * b
		case "/":
			return a / b if b != 0 else "unknown value"
		case default:
			return "unknown value"

print(calculator(1,2,"+"))
print(calculator(1,2,"-"))
print(calculator(3,5,"*"))
print(calculator(6,2,"/"))
print(calculator(2,0,"/"))
print(calculator(2,0,"$"))

def final_grade(exam, projects):
	if exam > 90 or projects > 10:
		return 100
	elif exam > 75 and projects >= 5:
		return 90
	elif exam > 50 and projects >= 2:
		return 75
	else:
		return 0

print(final_grade(100, 12))