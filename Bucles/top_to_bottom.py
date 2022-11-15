from yogi import read

a = read(int)
b = read(int)

if a>b:
    while a>b-1:
        print(a)
        a = a-1
elif b>a:
    while b>a-1:
        print(b)
        b = b-1
else: print(a)