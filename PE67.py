#PE67
#22/04/2017
#7273

tr_file=open("C:/Users/Arthur/Google Drive/Projets/Project Euler/PE67_triangle.txt","r")

tr=tr_file.readlines()
for i in range(len(tr)):
    tr[i]=(tr[i])[:len(tr[i])-1]

#Prend une liste de string représentant des nombres de deux chiffres
#et renvoie la liste de nombres correspondante

def conv_list(a):
    b=[]
    for i in range(0,len(a),3):
        aux=10*int(a[i])+int(a[i+1])
        b.append(aux)
    return b

for i in range(len(tr)):
    tr[i]=conv_list(tr[i])

#On peut considérer un algorithme du type diviser pour règner qui va
#calculer la quantité maximale pour chaque sous triangles et par
#conséquent diminuer le nombre de calculs
#Pour ce faire, on va utiliser un tableau pour stocker les valeurs des
#sous triangles correspondants

sous_tr=[k*[-1] for k in range(1,101)]

#Initialise la dernière ligne de sous_tr
n=len(sous_tr)-1
for j in range(len(sous_tr[n])):
    sous_tr[n][j]=tr[n][j]


#Calcule le plus grand chemin par mémoïsation partant de (i,j) (indice
#dans sous_tr)
def pgc_aux(i,j):
    if sous_tr[i][j]>=0:
        return sous_tr[i][j]
    else:
        sous_tr[i][j]=tr[i][j]+max(pgc_aux(i+1,j),pgc_aux(i+1,j+1))
        return sous_tr[i][j]

def pgc():
    return pgc_aux(0,0)
        