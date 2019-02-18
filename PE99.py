#PE99
#02/05/2017
#answer donne 708, mais la bonne réponse est 709 car on compte en nombre de ligne


#On utilise tout simplement le logarithme néperien qui permet de réduire les calculs



f=open("C:/Users/Arthur/Google Drive/Projets/Programmation/Project Euler/PE99_base_exp.txt","r")
num=f.readlines()

#Donne l'indice d'apparition de la première virgule dans une chaîne de caractères
def recherche_virgule(s):
    for i in range(len(s)):
        if s[i]==",":
            return i
    return 0

for i in range(len(num)):
    ind=recherche_virgule(num[i])
    num[i]=(int(num[i][:ind]),int(num[i][ind+1:len(num[i])-1]))

from math import *


#Retourne True si a**b>c**d
def compare(num1,num2):
    a,b=num1[0],num1[1]
    c,d=num2[0],num2[1]
    return b*log(a) > d*log(c)


def answer():
    #Memorize the indice of the biggest number
    m=0
    for i in range(1,len(num)):
        if compare(num[i],num[m]):
            m=i
    return m
    
