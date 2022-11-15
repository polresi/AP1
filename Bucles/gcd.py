from yogi import read

a = read(int)
b = read(int)
init__a = a
init__b = b

while (a!= b):
    if a> b: a = a - b
    else: b =  b - a       
print("The gcd of", init__a, "and", init__b, "is", a, end = "")
print(".")
"""
if a >= b:
    i = b
    while(not(a%i == 0 and b%i == 0)):
        i += -1
    print("The gdc of", a, "and", b, "is", i, end="")
    print(".")
else:
    i = a
    while(not(a%i == 0 and b%i == 0)):
        i += -1
    print("The gdc of", a, "and", b, "is", i, end="")
    print(".")
"""
