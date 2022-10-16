class Animals:
    def __init__(self, year, color):
        self.year = year
        self.color = color

    def walking(self):
        return "Go ahead!"


class Cats(Animals):
    def __init__(self, year, color, pur):
        super().__init__(year, color)
        self.__pur = pur

    def sound(self):
        return 'Meow'

    def walking(self):
        return "Go back"

    def get_pur(self):
        return f'pet me {self.__pur}'

    def set_pur(self, newpur):
        self.__pur = f'pet me {newpur}'


class Dogs(Animals):
    def __init__(self, year, color, bark, teeth):
        super().__init__(year, color)
        self.bark = bark
        self.teeth = teeth


Alligator = Animals(1984, 'black')
print(Alligator.year)

Deer = Animals(1990, 'yellow')
print(Deer.color)

Pushok = Cats(2018, 'red', 'purrrrpurrr')

print(Pushok.walking())
print(Pushok.get_pur())
print(Pushok.set_pur('RRRRrrrr'))

Shephard = Dogs(2020, 'white', 'Korea', 'auto')
print(Shephard.bark)
print(Shephard.walking())
