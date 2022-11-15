from yogi import read

b = read(int)
a = read(int)

if a >= b:
    while b < a:
        print(b, ",", sep="", end="")
        b = b+1
    print(a)
else: print()