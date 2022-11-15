from yogi import read
from turtle import *

n = read(int)
m = read(int)

for i in range(4):
    forward(m*n)
    left(90)

if n%2 == 0:
    for i in range((n)//2):
        forward(m)
        left(90)
        forward(m*n)
        right(90)
        forward(m)
        right(90)
        forward(m*n)
        left(90)
    left(90)
    for i in range((n)//2):
        forward(m)
        left(90)
        forward(m*n)
        right(90)
        forward(m)
        right(90)
        forward(m*n)
        left(90)
else:
    for i in range((n-1)//2):
        forward(m)
        left(90)
        forward(m*n)
        right(90)
        forward(m)
        right(90)
        forward(m*n)
        left(90)
    forward(m)
    left(90)
    for i in range((n-1)//2):
        forward(m)
        left(90)
        forward(m*n)
        right(90)
        forward(m)
        right(90)
        forward(m*n)
        left(90)




done()