class HomeWork2:
    def __init__(self, health, number, year, latter, replay):
        self.health = health
        self.number = number
        self.year = year
        self.latter = latter
        self.replay = replay

    def check_health(self):
        """Напишите программу, которая проверяет здоровье персонажа в игре.
            Если оно равно или меньше нуля, выведите на экран False, в противном случае True."""

        return False if self.health <= 0 else True

    def check_even_odd_number(self):
        """Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст
            'Четное', а иначе - 'Нечетное'"""

        return 'Четное число' if self.number % 2 == 0 else 'Нечетное число'

    def check_leap_year(self):
        """Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года, которые делятся
            без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). Однако, если год делится без остатка  на
             400, он также считается високосным (1200, 2000)"""

        return "Високосный год" if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0 \
            else "Невисокосный год"

    def replay_text(self):
        """Напишите программу, которая печатает введенный текст заданное количество раз, построчно. Текст и количество
            повторений нужно ввести с помощью input()"""
        for _ in range(self.replay):
            print(self.latter)


if __name__ == '__main__':
    health = int(input("Введите уровень здоровья Вашего героя: "))
    number = int(input("Введите любое число для проверки на четность: "))
    year = int(input("Введите год для проверки является ли год високосным : "))
    latter = input("Введите текст: ")
    replay = int(input("Введите число повторений введенного текста: "))
    hw = HomeWork2(health, number, year, latter, replay)
    print(hw.check_health())
    print(hw.check_even_odd_number())
    print(hw.check_leap_year())
    hw.replay_text()