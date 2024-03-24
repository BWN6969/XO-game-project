from turtle import *
from data import t
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
        penup()
        goto(x+20,y)
        pendown()
        begin_fill()
        lt(45)
        goto(z,d-20)
        lt(45)
        goto(z,d)
        lt(45)
        goto(z-20,d)
        lt(90)
        goto(x,y+20)
        lt(45)
        goto(x,y)
        end_fill()
    else :
        begin_fill()
        penup()
        goto(x-20,y)
        pendown()
        lt(45)
        goto(z,d-20)
        lt(45)
        goto(z,d)
        lt(45)
        goto(z+20,d)
        lt(90)
        goto(x,y+20)
        lt(45)
        goto(x,y)
        end_fill()
        
'''draw a hug ...'''

def hug(x,y):
    penup()
    goto(x,y)
    pendown()
    fillcolor('black')
    begin_fill()
    circle(75)
    end_fill()
    penup()
    goto(x,y+20)
    pendown()
    fillcolor("white")
    begin_fill()
    circle(55)
    end_fill()

''' draw boxs frame'''

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
    pendown()
    fd(300)
    l1Help()
    fd(600)
    l1Help()
    fd(300)
    end_fill()

''' gonna put where the limits at ...'''

def limitsPos():
    penup()
    pensize(5)
    bgcolor(choice(['pink','#66b3ff','#66ffc2','#CD5C5C','#6666ff','#d9b38c']))
    goto(125,0)
    frame()
    penup()
    goto(-125,0)
    left(90)
    frame()
    penup()
    goto(0,-100)
    left(-180)
    frame()
    penup()
    goto(0,100)
    left(90)
    frame()
    
    
