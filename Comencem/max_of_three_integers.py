from yogi import read

a = read(int)
b = read(int)
c = read(int)

if a >= b and a>=c:
    print(a)
elif b >= c and b >= a: 
    print(b)
else: 
    print(c)