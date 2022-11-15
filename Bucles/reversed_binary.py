from yogi import read

a = read(int)
result = ""
if a == 0:
    print("0")
else:
    while a != 0:
        if a%2 == 0:
            result = result + "0"
        else: 
            result = result + "1"
        a = a//2
    print(result)
