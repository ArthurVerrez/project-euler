#PE81
#03/05/2017
#427337

#On raisonne de la même manière que pour les triangles, on calcule les sous_sommes maximales pour les sous matrices

f=open("C:/Users/Arthur/Google Drive/Projets/Programmation/Project Euler/PE81_matrix.txt","r")
mat_text=f.readlines()

#Donne l'entier entre l'indice i inclu et le prochain indice de la virgule, renvoie alors l'indice d'après l'entier (on ne considère pas le dernier élement
def int_next_virg(s,i):
    a=""
    while i<len(s)-1:
        if s[i]==",":
            return int(a),i
        a+=s[i]
        i+=1
    return int(a),i

matr=[]
for s in mat_text:
    l=[]
    i=-1
    while i<len(s)-1:
        a,i=int_next_virg(s,i+1)
        l.append(a)
    matr.append(l)

#s[i][j] va représenter la somme maximale accessible à partir de (i,j)

from numpy import *
s=zeros((len(matr),len(matr)),int)

def remplit_s():
    s[len(s)-1,len(s)-1]=matr[len(s)-1][len(s)-1]

    for j in range(len(s)-2,-1,-1):
        s[len(s)-1,j]=matr[len(s)-1][j]+s[len(s)-1,j+1]
        s[j,len(s)-1]=matr[j][len(s)-1]+s[j+1,len(s)-1]
        
    for j in range(len(s)-2,-1,-1):
        for i in range(len(s)-2,-1,-1):
            s[i,j]=matr[i][j]+min((s[i,j+1],s[i+1,j]))
    