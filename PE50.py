#PE50
#30/12/2016
#997651

#On cherche les nombres premiers en dessous de m et on les range dans t
#On met dans tab[0,j] la somme du 1er nombre premier et des j suivants si cette somme est un nombre premier
#Puis dans tab[i,j] on met la somme du ieme nombre premier et des j-i suivants si elle est première
#On détermine ensuite le résultat en vérifiant les tab[i,j] > n par décroissance de j-i


def euclide(n):
###Renvoie un couple (p,b) de listes, p[i] donnant le i+1e nombre premier inférieur ou égal à n, b[i] renvoyant un booléen indiquant si i est premier
    b=[True for k in range(n+1)]
    p=[]
    b[0]=False
    b[1]=False
    for i in range(2,n+1):
        if b[i]:
            p.append(i)
            j=2
            while i*j <=n:
                b[i*j]=False
                j+=1
    return p

def prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**(1/2)+1),2):
        if n%i == 0:
            return False
    return True

import numpy as np
def alg(n,m):
    p=euclide(m)
    print("Euclide")
    a=len(p)
    tab=np.zeros((a,a),int)
    print("initialisation zéros")
    s=0
    #On remplit la première ligne
    for j in range(a):
        s+=p[j]
        tab[0,j]=s
    print("première ligne remplie")
    #On remplit les autres lignes
    for i in range(1,a):
        for j in range(i,a):
            tab[i,j]=tab[i-1,j]-p[i-1]
    print("autres lignes remplies")

    #On vérifie alors le plus grand nombre premier
    for j in range(a-1,-1,-1):
        for i in range(0,a-j):
            if tab[i,j+i] <= n and prime(tab[i,j+i]):
                #La première somme première que l'on trouve est la réponse
                return tab[i,j+i]

    
    
    
