'''
saisir_X
saisir_O
check_if_emp
check_if_win'''


from numpy import array as arr

''' saisir d'un place ...'''

def saisir(value):
    a = int(input(f"choisir votre emplacement {value} ="))
    while a>9 or a<1 or not ValueError:
        a = int(input(f"choisir votre emplacement {value} ="))
    return a

def saisir_place(value):
    c = saisir(format(f"{value}"))
    c-=1
    while tab[c] != "" :
        c = saisir(format(f"{value}"))
        c-=1
    return c


''' check if x or o won ...'''

def check_if_win(tab,elem):
    for i in range(0,len(tab),3):
        if tab[i]+tab[i+1]+tab[i+2] ==elem*3:
            return True
    for i in range(3):
        if tab[i]+tab[i+3]+tab[i+6] ==elem*3:
            return True
    if tab[0]+tab[4]+tab[8] ==elem*3 or tab[2]+tab[4]+tab[6]==elem*3:
        return True

    return False

''' check if there is no place to pick ...'''

def all_check_val(tab):
    for i in range(9):
        if tab[i] =="":
            return False
    return True

''' affichage ...'''

def afficher(tab):
    for i in range(0,len(tab),3):
        print(tab[i],"|",tab[i+1],"|",tab[i+2])
        
''' main function ...'''

def main(tab):
    tab[saisir_place(format("x"))] = "x"
    tab[saisir_place(format("o"))] = "o"
    while not(check_if_win(tab,"x")  and check_if_win(tab,"o")):
        tab[saisir_place(format("x"))] = "x"
        if check_if_win(tab,"x") :   #check if x won
            afficher(tab)
            print("x est gagné")
            break
        if all_check_val(tab) :
            afficher(tab)
            print("égalité")
            break
        tab[saisir_place(format("o"))] = "o"
        if check_if_win(tab,"o") :   #check if o won
            afficher(tab)
            print("o est gagné")
            break
        if all_check_val(tab) :
            afficher(tab)
            print("égalité")
            break
        afficher(tab)
        
tab = arr([str()]*9)