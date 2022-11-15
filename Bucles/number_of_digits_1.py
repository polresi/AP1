from yogi import read

a = read(int)
b =0
c = a
if c != 0:
    while c > 0:
        c = c//10
        b = b +1
    print("The number of digits of", a, "is", b,end="") 
    print(".")
else:
    print("The number of digits of", 0, "is", 1, end="")
    print(".")