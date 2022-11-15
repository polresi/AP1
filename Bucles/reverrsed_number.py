from yogi import read


a = read(int)
stri = ""

if a == 0:
    print("0")
else:    
    while a != 0:
        rem = a%10
        stri = stri + str(rem)
        a = a//10
    print(stri)