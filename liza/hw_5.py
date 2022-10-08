class Animal:
    def __init__(self, name, is_adult):
        self.name = name
        self.is_adult = is_adult

    def weight(self):
        pass

    def get_is_adult(self):
        if self.is_adult:
            return 'I am big!'
        else:
            return 'i  am  small!'

class Cat(Animal):
    def __init__(self, name, is_adult, weight):
        super(Cat, self).__init__(name, is_adult)
        self.__voice = 'Miau!'
        self.weight = weight

    def get_voice(self):
        return self.__voice

    def get_weight(self):
        return f'I weight {self.weight} kg!\n'


class Mouse(Animal):
    def __init__(self, name, is_adult, weight):
        super(Mouse, self).__init__(name, is_adult)
        self.weight = weight
        self.__voice = 'Peeeee!'

    def get_voice(self):
        return self.__voice

    def get_weight(self):
        return f'I weight {self.weight} kg!\n'


vasya = Cat('Vasily', True, 5)
print(vasya.name, vasya.get_voice())
print(vasya.get_is_adult())
print(vasya.get_weight())

mikki = Mouse('Mikki', False, 0.3)
print(mikki.name, mikki.get_voice())
print(mikki.get_is_adult())
print(mikki.get_weight())
