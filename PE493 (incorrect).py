#PE493
#03/05/2017


from random import *
#Essayons une première méthode qui est d'approximer par plein d'essais informatiques

#Même si l'énoncé est très mauvais, on considerera qu'il n'y a pas de remise de la balle

#A une liste urne donnée de taille 7 représentant l'urne (l[i] donne le nombre de boules de couleur i), on associe egalement une liste_non vide qui donne les indices des couleurs dont il reste des boules et n le nombre de boules total restantes
def pick_ball(urne,non_vide,n):
    l=[urne[non_vide[0]]/n]
    for i in range(1,len(non_vide)):
        l.append(urne[non_vide[i]]/n +l[i-1])
        
    al=random()
    i=0
    while l[i]<al:
        i+=1
    urne[non_vide[i]]-=1
    r=non_vide[i]
    if urne[non_vide[i]]==0:
            del(non_vide[i])
    return r



#Renvoie le nombre de balle différentes au bout de 20 prises
def test():
    urne=[10 for k in range(7)]
    non_vide=[k for k in range(7)]
    diff=[]
    n=70
    for i in range(20):
        r=pick_ball(urne,non_vide,n)
        n-=1
        if not r in diff:
            diff.append(r)
    return len(diff)

def moyenne_diff_color(n):
    s=0
    for i in range(n):
        s+=test()
    return s/n
    
            
            