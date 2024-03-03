from turtle import *
from draw import box



'''draw boxs's frame ...'''

def draw_boxs():
    penup()
    goto(-285,135)
    x =-285
    y = 135
    pendown()
    for k in range(3):
        for j in range(3):
            box()
            penup()
            left(-90)
            fd(60)
            pendown()
        penup()
        goto(x,y-215)
        y -=215
        pendown()