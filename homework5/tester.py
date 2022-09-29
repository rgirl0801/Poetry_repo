from human import Human

class Tester(Human):

    def __init__(self, name, age, sex, language):
        super().__init__(name, age, sex)
        self.__language = language

    def test(self):
        return print("I do-do-doooo.")

    def get_language(self):
        return print("My language is {}.".format(self.__language))

    def set_language(self, newlang):
        self.__language = newlang
