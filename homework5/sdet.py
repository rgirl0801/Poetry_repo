from tester import Tester


class Sdet(Tester):

    def __init__(self, name, age, sex, language, codlang):
        super().__init__(name, age, sex, language)
        self.__codlang = codlang

