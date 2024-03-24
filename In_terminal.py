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

def check_if_win(x,z):
    for i in range(0,len(x),3):
        a = x[i]+x[i+1]+x[i+2] ==z*3
        if a :
            return a
    for i in range(0,3):
        a = x[i]+x[i+3]+x[i+6] ==z*3
        if a :
            return a
    a  = x[0]+x[4]+x[8] ==z*3
    if a :
        return a
    a  = x[2]+x[4]+x[6]==z*3
    if a :
        return a
    return False

''' check if there is no place to pick ...'''

def all_check_val(tab):
    for i in range(9):
        if tab[i] =="" :
            return False
    return True

''' affichage ...'''

def afficher(a):
    for i in range(0,len(a),3):
        print(a[i],"|",a[i+1],"|",a[i+2])
        
''' main function ...'''

def main(tab):
    tab[saisir_place(format("x"))] = "x"
    tab[saisir_place(format("o"))] = "o"
    while not(check_if_win(tab,"x")  and check_if_win(tab,"o")):
        tab[saisir_place(format("x"))] = "x"
        a = check_if_win(tab,"x")        #check if x won
        if a :
            afficher(tab)
            print("x est gagné")
            break
        if all_check_val(tab) :
            afficher(tab)
            print("égalité")
            break
        tab[saisir_place(format("o"))] = "o"
        a = check_if_win(tab,"o")     #check if o won
        if a :
            afficher(tab)
            print("o est gagné")
            break
        if all_check_val(tab) :
            afficher(tab)
            print("égalité")
            break
        afficher(tab)
        
tab = arr([str()]*9)