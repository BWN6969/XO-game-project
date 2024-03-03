from numpy import array
from turtle import*
from In_terminal import all_check_val,check_if_win,tab
global t

t = array([dict(boxN = int(),boxPosX_ini = float(),boxPosY_ini = float(),boxPosX = float(),boxPosY = float(),empty=True)]*9)
t[0] =dict(boxN = int(),boxPosX_ini = float(),boxPosY_ini = float(),boxPosX = float(),boxPosY = float(),empty=True)
t[0]["boxN"] =0
t[0]["boxPosX_ini"] =-285
t[0]["boxPosY_ini"] =135
t[0]["boxPosX"] =-135
t[0]["boxPosY"] =285

''' get buttons location,number,state ...'''

def fill(t):
    for i in range(1,9):
        t[i] =dict(boxN = int(),boxPosX_ini = float(),boxPosY_ini = float(),boxPosX = float(),boxPosY = float(),empty=True)
        t[i]["boxN"] =i
        t[i]["boxPosX_ini"] =t[i-1]["boxPosX_ini"] + 210
        t[i]["boxPosY_ini"] =t[i-1]["boxPosY_ini"] 
        t[i]["boxPosX"] =t[i]["boxPosX_ini"] + 150
        t[i]["boxPosY"] =t[i]["boxPosY_ini"] +150
        if i%3==0:
            t[i]["boxN"] =i
            t[i]["boxPosX_ini"] =-285
            t[i]["boxPosY_ini"] =t[i-3]["boxPosY_ini"] -215
            t[i]["boxPosX"]=t[i]["boxPosX_ini"]+150
            t[i]["boxPosY"] =t[i]["boxPosY_ini"]+150

'''check if there is no place to pick ...'''

def all_check(t):
    for i in range(9):
        if t[i]["empty"] :
            return False
    return True

'''check win or equality ...'''

def main(tab):
    a = check_if_win(tab,"x")        #check if x won
    if a :
        return "x est gagné"
    if all_check_val(tab) :
        return "égalité"
    a = check_if_win(tab,"o")     #check if o won
    if a :
        return "o est gagné"
    if all_check_val(tab) :
        return "égalité"
fill(t)