
def gcd_mod(a, b):
    while a  > 0 and b >0:
        if a>= b:
            c = b
            a = a%b
        else:
            c = a
            b = b%a
    return c

from yogi import read
print(gcd_mod(read(int), read(int)))


