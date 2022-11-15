from turtle import *
from yogi import read

a = read(str)

if a == "cercle":
    b = read(int)
    circle(b)
elif a == "quadrat":
    b = read(int)
    for i in range(4):
        forward(b)
        left(90)
elif a == "rectangle":
    b = read(int)
    c = read(int)
    for i in range(2):
        forward(b)
        left(90)
        forward(c)
        left(90)
        
done()
