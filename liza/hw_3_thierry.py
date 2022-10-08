#  1kb = 2 ** 10
#  1Mb = 2 ** 20
#  1Gb = 3 ** 30
#  1Tb = 2 ** 40
import os.path


def user_friendly_size(b):
    if b >= (2 ** 40):
        return f'{round(b / (2 ** 40), 2)} Tb'
    elif b >= (2 ** 30):
        return f'{round(b / (2 ** 30), 2)} Gb'
    elif b >= (2 ** 20):
        return f'{round(b / (2 ** 20), 2)} Mb'
    elif b >= (2 ** 10):
        return f'{round(b / (2 ** 10), 2)} kb'
    else:
        return f'{b} b'

print(user_friendly_size(9999))
print(user_friendly_size(9999999))
print(user_friendly_size(955))
print(user_friendly_size(9845610865445))
print(user_friendly_size(os.path.getsize('/Users/liza/PycharmProjects/Python_Li_1/test_1.txt')))
print(user_friendly_size(os.path.getsize('/Users/liza/Documents/Foto/Kotiki.jpg')))
print(user_friendly_size(os.path.getsize('/Users/liza/Documents/Foto/avstrija-18/IMG_20180113_144440.jpg')))
