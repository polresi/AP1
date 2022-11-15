from yogi import read 

a = read(int)

if a < 10:
    print("it's cold")
    if a < 1:
        print("water would freeze")
elif a > 30:
    print("it's hot")
    if a > 99:
        print("water would boil")
else:
    print("it's ok")
