from turtle import *
from data import t

''' draw a cube ...'''

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
