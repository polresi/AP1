from yogi import read

a1 = read(int)
a2 = read(int)
b1 = read(int)
b2 = read(int)


if (a1 < b1 and a2 < b1) or (b1 < a1 and b2 < a1):
    print("[]")
elif (a1 >= b1 and a2 <= b2):
    print("[", a1, ",", a2, "]", sep="")
elif (b1 >= a1 and b2 <= a2):
    print("[", b1, ",", b2, "]", sep="")
elif (a1 >= b1 and b2 <= a2):
    print("[", a1, ",", b2, "]", sep="")
elif (a1<= b1 and a2 <= b2):
    print("[", b1, ",", a2, "]", sep="")
