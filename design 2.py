from turtle import *
from colorsys import *

tracer(50)
bgcolor('gray')
pensize(2)
h = 0 

for i in range(60):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.01
    for j in range(9):
        circle(140, 90)
        left(160)
        circle(80, 90)
        left(160)
    right(89)
done         