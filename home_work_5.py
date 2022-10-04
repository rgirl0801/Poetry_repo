""" Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
    - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
    нужно использовать методы get и set"""


class Animal:
    def __init__(self, view_animal, breed_animal, weight, height):
        self.__view_animal = view_animal
        self.__breed_animal = breed_animal
        self.height = height
        self.weight = weight

    def set_attr_animal(self, view_animal, breed_animal):
        self.__view_animal = view_animal
        self.__breed_animal = breed_animal

    def get_attr_animal(self):
        return self.__view_animal, self.__breed_animal

    def get_size_the_animal(self):
        if 1 <= self.weight <= 4 and 1 <= self.height <= 3:
            return "Маленькое животное"
        if 5 <= self.weight <= 7 and 4 <= self.height <= 5:
            return "Среднее животное"
        if 8 <= self.weight <= 10 and 6 <= self.height <= 7:
            return "Бльшое животное"


class Cat(Animal):
    def __init__(self, view_animal, breed_animal, height, weight, name, food):
        super().__init__(view_animal, breed_animal, height, weight)
        self.food = food
        self.name = name

    def get_view_and_breed_a_cat(self):
        attr_cat = self.get_attr_animal()
        return attr_cat

    def get_size_the_animal(self):
        if 1 <= self.weight <= 4 and 1 <= self.height <= 3:
            return f"{self.name} маленькая кошка"
        if 5 <= self.weight <= 7 and 4 <= self.height <= 5:
            return f"{self.name} средняя кошка"
        if 8 <= self.weight <= 10 and 6 <= self.height <= 7:
            return f"{self.name} большая кошка"

    def cat_likes_eat(self):
        return f"Кошка {self.name} любит есть {self.food}"

    def how_a_cat_meows(self, volume):
        return f"Кошка {self.name} умеет {volume} мяукать"


class Dog(Animal):
    def __init__(self, view_animal, breed_animal,  weight, height, name, food, prise_dog):
        super().__init__(view_animal, breed_animal,  weight, height)
        self.food = food
        self.name = name
        self.__prise_dog = prise_dog

    def get_view_and_breed_a_dog(self):
        attr_dog = self.get_attr_animal()
        return attr_dog

    def set_attr_prise(self, prise_dog):
        self.__prise_dog = prise_dog

    def get_attr_prise(self):
        return self.__prise_dog

    def get_size_the_animal(self):
        if 1 <= self.weight <= 4 and 1 <= self.height <= 3:
            return f"{self.name} маленькая собака"
        if 5 <= self.weight <= 7 and 4 <= self.height <= 5:
            return f"{self.name} средняя собака"
        if 8 <= self.weight <= 10 and 6 <= self.height <= 7:
            return f"{self.name} большая собака"

    def dog_likes_eat(self):
        return f"Собака {self.name} любит есть {self.food}"

    def how_a_dog_bark(self, volume):
        return f"Собака {self.name} умеет {volume} лаять"

    def get_price_dog(self):
        return f"Собака {self.name} стоит {self.__prise_dog} уе"


if __name__ == '__main__':
    cat1 = Cat("Домашняя", "Бенгальская", 1, 1, "Барсик", "Kитикет")
    print(f'Кошку зовут - {cat1.name}')
    print('Вид кошки: {}, порода кошки: {}'.format(cat1.get_view_and_breed_a_cat()[0],
                                                   cat1.get_view_and_breed_a_cat()[1]))
    print(cat1.get_size_the_animal())
    print(f"{cat1.cat_likes_eat()} и {cat1.how_a_cat_meows('Громко')}")
    cat1.set_attr_animal("Изгой", "Вислоухая")
    cat1.name = "Жмурик"
    cat1.food = "Мясо"
    cat1.height = 5
    cat1.weight = 5
    print(f'Кошку зовут - {cat1.name}')
    print('Вид кошки: {}, порода кошки: {}'.format(cat1.get_view_and_breed_a_cat()[0],
                                                   cat1.get_view_and_breed_a_cat()[1]))
    print(cat1.get_size_the_animal())
    print(f"{cat1.cat_likes_eat()} и {cat1.how_a_cat_meows('громко')}")

    cat2 = Cat("Дикая", "Дворовая", 9, 6, "Чёрно-белая", "что придется")
    print('Вид кошки: {}, порода кошки: {}'.format(cat2.get_view_and_breed_a_cat()[0],
                                                   cat2.get_view_and_breed_a_cat()[1]))
    print(cat2.get_size_the_animal())
    print(f"{cat2.cat_likes_eat()} и {cat2.how_a_cat_meows('громко')}")
    cat2.set_attr_animal("Дикая", "Подвальная")
    cat2.name = "Мироместин"
    cat2.food = "микробы"
    cat2.height = 3
    cat2.weight = 4
    print('Вид кошки: {}, порода кошки: {}'.format(cat2.get_view_and_breed_a_cat()[0],
                                                   cat2.get_view_and_breed_a_cat()[1]))
    print(f'Кошку зовут - {cat2.name}')
    print(cat2.get_size_the_animal())
    print(f"{cat2.cat_likes_eat()} и {cat2.how_a_cat_meows('тихо')}")

    dog1 =Dog("Домашний","Доберман", 6, 4, "Буцифал", "конфеты",100)
    print(f'Собаку зовут - {dog1.name}')
    print('Вид собаки: {}, порода собаки: {}'.format(dog1.get_view_and_breed_a_dog()[0],
                                                   dog1.get_view_and_breed_a_dog()[1]))

    print(dog1.get_size_the_animal())
    print(dog1.dog_likes_eat())
    print(dog1.how_a_dog_bark("очень громко"))
    print(dog1.get_price_dog())
    dog1.set_attr_animal('Дворовая','Волкодав')
    dog1.food = "собак"
    dog1.name = "Разрушитель"
    dog1.set_attr_prise(50)
    print(f'Собаку зовут - {dog1.name}')
    print('Вид собаки: {}, порода собаки: {}'.format(dog1.get_view_and_breed_a_dog()[0],
                                                     dog1.get_view_and_breed_a_dog()[1]))

    print(dog1.get_size_the_animal())
    print(dog1.dog_likes_eat())
    print(dog1.how_a_dog_bark("тихо"))
    print(dog1.get_price_dog())






