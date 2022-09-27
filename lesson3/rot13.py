# https://www.codewars.com/kata/52223df9e8f98c7aa7000062
def rot13(message):
    res = ''
    input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    for ch in message:
        if ch in input:
            res += output[input.index(ch)];
        else:
            res += ch;
    return res

print(rot13("EBG13 rknzcyr.")) # ROT13 example
print(rot13("This is my first ROT13 excercise!")) # Should return "Guvf vf zl svefg EBG13 rkprepvfr!"
print(rot13("123")) # Should return "123"
