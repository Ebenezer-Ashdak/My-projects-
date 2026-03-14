from turtle import *
from colorsys import *


tracer(50)
bgcolor('black')
pensize(2)
h = 0 

for i in range(60):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.1
    for j in range(9):
        circle(80, 180)
        left(60)
        circle(80, 180)
        left(60)
    right(80)
done         