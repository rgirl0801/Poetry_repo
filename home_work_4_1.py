def count_move(s):
    values = {"F": 0, "U": 1, "D": -1}
    level, valley = 0, 0
    for ch in s:
        if level == -1 and ch =="U":
            valley +=1
        level += values[ch]
    return valley


print(count_move("UFFFD"))
print(count_move("DFFFD"))
print(count_move("DFFFU"))
print(count_move("UFFFU"))
print(count_move("UFFDDFDUDFUFU"))
print(count_move("UFFDDFDUDFUFUUFFDDFDUDFUFU"))
print(count_move("UFFDDFDUDFUFUUFFDDUFFDDUFFDDUDUDUDUDUDUUUUUUUUU"))
print(count_move("UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU"))
print(count_move("UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU"))



