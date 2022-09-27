# https://www.codewars.com/kata/5da9973d06119a000e604cb6/train/python
def counting_valleys(s):
    count = 0
    level = 0
    for i in s:
        if i == 'U':
            if level == -1:
                count += 1
            level += 1
        elif i == 'D':
            level -= 1
    return count

print(counting_valleys('UFFFD')) # 0
print(counting_valleys('DFFFD')) # 0
print(counting_valleys('UFFFU')) # 0
print(counting_valleys('DFFFU')) # 1
print(counting_valleys('UFFDDFDUDFUFU')) # 1
print(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFU')) # 2