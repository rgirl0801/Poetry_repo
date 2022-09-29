# Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
# как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
# нужно использовать методы get и set

from human import Human
from tester import Tester
from sdet import Sdet


tester1 = Tester("Peter", "31", "Male", "Russian")
tester1.speak("Tester")
tester1.test()
tester1.get_language()
tester1.set_language("English")
tester1.get_language()
tester1.print_info()
tester1.set_name("Maxim")
tester1.set_age("15")
tester1.set_sex("Woman")
tester1.print_info()
human2 = Human()
human2.print_info()
sdet1 = Sdet("Maria", 41, "Woman", "Polish", "Java")
sdet1.print_info()
sdet1.set_age("99")
sdet1.print_info()
