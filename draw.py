from turtle import *
from random import choice

''' draw a box ...'''

def box():
    for i in range(5):
        fd(150)
        lt(90)

'''draw a label frame ...'''

def label_frame():
    penup()
    goto(-150,-330)
    pendown()
    fillcolor("black")
    begin_fill()
    goto(150,-330)
    goto(150,-380)
    goto(-150,-380)
    goto(-150,-330)
    end_fill()
    
''' write a text ...'''

def label(text,x):
    penup()
    goto(x,-370)
    pendown()
    pencolor("white")
    write(text,font=("verdana",20))
    pencolor('black')
    
''' draw a kiss ...'''

def kiss(x,y,z,d,n):
    fillcolor('black')
    if n==0:
        pu()
        goto(x+20,y)
        pd()
        begin_fill()
        lt(45)
        goto(z,d-20)
        circle(14.32,180)
        goto(z-20,d)
        goto(x,y+20)
        circle(14.32,180)
        end_fill()
    else : 
        begin_fill()
        pu()
        goto(x-20,y)
        pd()
        lt(45)
        goto(z,d-20) 
        lt(45)
        circle(-14.32,180)
        goto(z+20,d)
        goto(x,y+20)
        circle(-14.32,180)
        end_fill()

'''draw a hug ...'''

def hug(x,y,color_inside):
    pu()
    goto(x,y)
    pd()
    fillcolor('black')
    begin_fill()
    circle(75)
    end_fill()
    pu()
    goto(x,y+20)
    pd()
    fillcolor(color_inside)
    begin_fill()
    circle(55)
    end_fill()

''' draw boxs frame'''

def draw_boxs():
    pu()
    goto(-285,135)
    x =-285
    y = 135
    pd()
    for k in range(3):
        for j in range(3):
            box()
            penup()
            left(-90)
            fd(60)
            pendown()
        pu()
        goto(x,y-215)
        y -=215
        pd()
        
        
''' syntax decrease ...'''

def l1Help():
    lt(90)
    fd(25)
    lt(90)
    
''' gonna build the limits ...'''

def frame():
    fillcolor('black')
    begin_fill()
    lt(90)
    pd()
    fd(300)
    l1Help()
    fd(600)
    l1Help()
    fd(300)
    end_fill()

''' gonna put where the limits at ...'''

def limitsPos():
    pu()
    pensize(5)
    x =choice(['pink','#66b3ff','#66ffc2','#CD5C5C','#6666ff','#d9b38c','#FF8A08','#77B0AA','#0C2D57','#FFFAB7'])
    bgcolor(x)
    goto(125,0)
    frame()
    pu()
    goto(-125,0)
    left(90)
    frame()
    pu()
    goto(0,-100)
    left(-180)
    frame()
    pu()
    goto(0,100)
    left(90)
    frame()
    return x

    
