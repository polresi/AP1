from yogi import read

a = read(int)
i = 2

while a!= 1:
    while a%i == 0:
        a = a//i
        print(i)
    i=i+1