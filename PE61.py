#PE61
#04/05/2017
#On trouve [8256, 5625, 2512, 1281, 8128, 2882] donc 28684


N=19
M=141
#Juste un nombre déterminant la limite de recherche de cherche de sorte à avoir surtout des P de 4 chiffres
#On a que P(_,n) croissant
#et P(8,18)<1000 et P(3,141)>9999
def P(i,n):
    if i==3:
        return n*(n+1)//2
    if i==4:
        return n**2
    if i==5:
        return n*(3*n-1)//2
    if i==6:
        return n*(2*n-1)
    if i==7:
        return n*(5*n-3)//2
    if i==8:
        return n*(3*n-2)

#On va rechercher les nombres en raisonnant selon l'ordre d'apparition de triangle, square, pentagonal...
#On va donc les chercher selon des listes l=[a,b,c,d,e,f] avec l[j] représentant quel i dans P(i,_) aura la jeme place dans la recherche

#Vérifie si les deux derniers chiffres de a sont les mêmes que les deux premiers chiffres de b
def cycl(a,b):
    return str(a)[-2:]==str(b)[:2]


def cherche(pl):
    for i in range(N,M):
        ai=P(pl[0],i)
        if ai>999 and ai<10000:
            for j in range(N,M):
                aj=P(pl[1],j)
                if aj>999 and aj<10000 and cycl(ai,aj):
                    for k in range(N,M):
                        ak=P(pl[2],k)
                        if ak>999 and ak<10000 and cycl(aj,ak):
                            for l in range(N,M):
                                al=P(pl[3],l)
                                if al>999 and al<10000 and cycl(ak,al):
                                    for m in range(N,M):
                                        am=P(pl[4],m)
                                        if am>999 and am<10000 and cycl(al,am):
                                            for n in range(N,M):
                                                an=P(pl[5],n)
                                                if an>999 and an<10000 and cycl(am,an) and cycl(an,ai):
                                                    return True,[ai,aj,ak,al,am,an]
    return False,[]


#Maintenant il suffit de savoir donner toutes les permutations de [3,4,5,6,7,8] et de tout vérifier un à un jusqu'à trouver le bon
#Pour information, il y en a 6!=720

#Pour ce faire, on vole cette fonction de PE24

#perm ne contient pas x
def permutations_aux(x,perm):

    if len(x) == 2:
        perm.append(x)
        perm.append(x[::-1])
    else:
        for i in range(len(x)):
            y=x
            y[0],y[i]=y[i],y[0]
            perm_y=[]
        
            permutations_aux(y[1::],perm_y)
        
            for j in range(len(perm_y)):
                perm.append([y[0]]+perm_y[j])

def permutations(x):
    p=[]
    permutations_aux(x,p)
    return p

def answer():
    perm=permutations([3,4,5,6,7,8])
    for p in perm:
        a=cherche(p)
        if a[0]:
            return a[1]

#Il y a apparemment eu une incompréhension du sujet, il semblerait que les nombres ne doivent pas être square s'ils sont heptagonal etc...

#On va donc garder toutes les possibilités dans une liste

def answers_list():
    perm=permutations([3,4,5,6,7,8])
    poss=[]
    for p in perm:
        a=cherche(p)
        if a[0]:
            poss.append(a[1])
    return poss

#On réalise maintenant des fonctions vérifiant si un nombre est d'un certain type

#Renvoie True si a est du type i
def type(a,i):
    n=1
    while P(i,n)<a:
        n+=1
    return P(i,n)==a

def which_type(a):
    t=[]
    for i in range(3,9):
        if type(a,i):
            t.append(i)
    return t

def convient(ans):
    for a in ans:
       if len(which_type(a))>1: 
           return False
    return  True

def final_ans(l_ans):
    for ans in l_ans:
        if convient(ans):
            return ans

#Finalement il n'y a pas vraiment eu de mauvaise interprétation du sujet, c'est juste que j'avais fait une erreur dans l'écriture de P(7,_)
    



        
                
            