''' import packages ...'''

from import_pack import *

''' starting phase ...'''

labF()
label("starting ...",-80)
speed(15)
color = limitsPos()
pensize(1)
draw_boxs()
a = choice(["X","O"])
labF()
label(f"{a} turn ",-45)
hideturtle()




''' clickable buttons ...'''

def check_butt(x,y):
    global a
    global tab
    for i in range(9):
        if x>=t[i]["boxPosX_ini"] and x<=t[i]["boxPosX"] and y>=t[i]["boxPosY_ini"] and y<=t[i]["boxPosY"]:
            if t[i]["empty"] :
                if a=="O" :
                    tab[i] = "o"
                    labF()
                    setheading(0)
                    hug(t[i]["boxPosX"]-75,t[i]["boxPosY_ini"],color)
                    if main(tab):
                        labF()
                        if main(tab) =="draw":
                            step = -35
                        else:
                            step = -45
                        label(f"{main(tab)}",step)
                        sleep(1)
                        exit()
                    else:
                        a = "X"
                        label(f"{a} turn ",-45)
                    
                else:
                    tab[i] = "x"
                    kiss(t[i]["boxPosX_ini"],t[i]["boxPosY_ini"],t[i]["boxPosX"],t[i]["boxPosY"],0)
                    setheading(0)
                    kiss(t[i]["boxPosX"],t[i]["boxPosY_ini"],t[i]["boxPosX_ini"],t[i]["boxPosY"],1) 
                    if main(tab):
                        labF()
                        if main(tab) =="draw":
                            step = -35
                        else:
                            step = -45
                        label(f"{main(tab)}  ",step)
                        sleep(1)
                        exit()
                    else:
                        labF() 
                        a = "O"
                        label(f"{a} turn ",-45)
                    
                t[i]["empty"] = False
            else:  
                labF()
                label("place already taken",-135)

                            
onscreenclick(check_butt)




