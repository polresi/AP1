from turtle import forward
from yogi import read
from turtle import *

n = read(int)
m = read(int)
i = 1

while i <= n:
    forward(m*i)
    left(90)
    forward(m*i)
    left(90)
    i = i+1

done()