from yogi import read

h = read(int)
m = read(int)
s = read(int)

s = s+1
if s == 60:
    m = m+1
    if m == 60:
        h = h+1

a = s%60
b = m%60
c = h%24

if a<10:
    a = str(a)
    a = "0" + a
if b<10:
    b = str(b)
    b = "0" + b
if c<10:
    c = str(c)
    c = "0" + c


print(c,":",b,":",a,sep="")






