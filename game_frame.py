from random import choice
from turtle import *

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
