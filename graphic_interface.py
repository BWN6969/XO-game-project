''' import packages ...'''

from import_pack import *
labF()
label("starting ...",-80)
speed(15)
limitsPos()
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
            print(t[i]["boxN"])
            penup()
            goto(t[i]["boxPosX"]-75,(t[i]["boxPosY_ini"]))
            pendown()
            print(t[i]["boxPosX_ini"]-t[i]["boxPosX"],t[i]["boxPosY_ini"]-t[i]["boxPosY"])
            if t[i]["empty"] :
                if a=="O" :
                    tab[i] = "o"
                    print(tab)
                    labF()
                    setheading(0)
                    hug(t[i]["boxPosX"]-75,t[i]["boxPosY_ini"])
                    if main(tab):
                        '''win_col(t[i]["boxPosX_ini"],t[i]["boxPosY"],t[i]["boxPosY"]'''
                        labF()
                        label(f"{main(tab)}  ",-100)
                        sleep(1)
                        exit()
                    else:
                        a = "X"
                        label(f"{a} turn ",-45)
                    
                else:
                    tab[i] = "x"
                    print(tab)
                    kiss(t[i]["boxPosX_ini"],t[i]["boxPosY_ini"],t[i]["boxPosX"],t[i]["boxPosY"],0)
                    setheading(0)
                    kiss(t[i]["boxPosX"],t[i]["boxPosY_ini"],t[i]["boxPosX_ini"],t[i]["boxPosY"],1) 
                    if main(tab):
                        labF()
                        label(f"{main(tab)}  ",-100)
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
            
            if all_check(t):
                print("égalité")
            print(t)
           
            

            
            
onscreenclick(check_butt)



