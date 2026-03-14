from turtle import *
from colorsys import *

tracer(60)
bgcolor('black')
pensize(1)
h = 0 

for i in range(900):
    color(hsv_to_rgb(h, 1, 1))
    h = (h + 0.005) %1
    for j in range(9):
        backward(50 + i /3)
        right(60)
    right(1)
done         