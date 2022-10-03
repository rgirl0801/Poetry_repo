# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set
class Person:
		def __init__(self, name, age):
				self.name = name
				self.age = age
				self.__salary = 0

		def get_salary(self):
				return self.__salary

		def set_salary(self, salary):
				self.__salary = salary

class Employee(Person):
		def __init__(self, name, age, position):
				super().__init__(name, age)
				self.position = position

class Manager(Employee):
		def __init__(self, name, age, position, department):
				super().__init__(name, age, position)
				self.department = department

class Director(Manager):
		def __init__(self, name, age, position, department, company):
				super().__init__(name, age, position, department)
				self.company = company

		def __str__(self) -> str:
			return f"Director {director.name} is {director.age} years old, works as {director.position} in {director.department} department of {director.company} company and earns {director.get_salary()} dollars per month."

print("=" * 40 + " GOOGLE " + "=" * 40)
director = Director('John', 45, 'Director', 'IT', 'Google')
director.set_salary(100000)
# print(f"Director {director.name} is {director.age} years old," +
# 	f" works as {director.position} in {director.department} department of {director.company} company" +
# 	f" and earns {director.get_salary()} dollars per month.");
print("-" * 40 + " DIRECTOR " + "-" * 40)
print(str(director))

manager = Manager('Mike', 35, 'Manager', 'IT')
manager.set_salary(50000)
print("-" * 40 + " MANAGER " + "-" * 40)
print(f"Manager {manager.name} is {manager.age} years old," +
	f" works as {manager.position} in {manager.department} department and earns {manager.get_salary()} dollars per month.");

employee1 = Employee('Tom', 25, 'Engineer')
employee1.set_salary(20000)
print("-" * 40 + " EMPLOYEE 1 " + "-" * 40)
print(f"Employee {employee1.name} is {employee1.age} years old," +
	f" works as {employee1.position} and earns {employee1.get_salary()} dollars per month.");

employee2 = Employee('Bob', 30, 'Engineer')
employee2.set_salary(15000)
print("-" * 40 + " EMPLOYEE 2 " + "-" * 40)
print(f"Employee {employee2.name} is {employee2.age} years old," +
	f" works as {employee2.position} and earns {employee2.get_salary()} dollars per month.");

# 5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий
