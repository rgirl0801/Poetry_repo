from string import digits
import re

s = 'E3at m2e2!!'
s1 = 'Dsa32 cdsc34232 csa!!! 1I 4Am cool!'
s2 = '33333Ad2dsad3ds21 A3333  1$$s122a!d! A2!A!3Ae$24 f2##222 '


def string_clean(s):
    """Решено через цикл for"""
    num = digits
    res = ''.join([i for i in s if i not in num])
    return res


def str_clr(l):
    """Решено через регулярку"""
    res = re.sub('\d', '', l)
    return res


print(string_clean(s1))
print(str_clr(s2))
