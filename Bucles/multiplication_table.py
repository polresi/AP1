from yogi import read

a = read(int)
for i in range(10):
    v = a*(i+1)
    print(a,"*",i+1," = " ,v, sep="")