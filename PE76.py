#PE76
#30/04/2017
#190569291

#Représentera les différentes sommations par des listes croissantes
#On a toujours a=a*1=1+1+...+1 (a fois), ce sera le commencement de tout calcul de sommation

#Renvoie l'ensemble des sommations possibles suivantes, dans l'ordre lexicographique
def next_poss(l):
    if len(l)<=2:
        return []
    ens=[l[:len(l)-2]+[l[len(l)-1]+l[len(l)-2]]]
    
    for i in range(len(l)-3,-1,-1):
        if l[i]+l[i+1]<=l[i+2]:
            ens.append(l[:i]+[l[i]+l[i+1]]+l[i+2:])
    return ens


#Pour éviter les doublons, on va trier l par ordre croissant et raisonner par dichotomie

def answer(N=100):
    
    l=[[1 for k in range(N)]]
    tot=l.copy()
    p_next=[]
    r=0
    while len(l)>0:
        for a in l:
            for i in next_poss(a):
                if not recherche_dicho(tot,i):
                    p_next.append(i)
                    tot=inserer_dicho(tot,i)
        l=p_next.copy()
        
        p_next=[]
    return tot

def answer_bis(N=100):
    l=[[1 for k in range(N)]]
    #Contient à tot[k] l'ensemble des sommations de taille k
    tot=[[] for k in range(N+1)]
    tot[N]=[l.copy()]
    p_next=[]
    r=0
    k=N
    while len(l)>0:
        k-=1
        for a in l:
            for i in next_poss(a):
                if not recherche_dicho(tot[k],i):
                    p_next.append(i)
                    tot[k]=inserer_dicho(tot[k],i)
        l=p_next.copy()
        
        p_next=[]
    return tot
 
def answer_num(N=100):
    tot=answer_bis(N)
    return sum([len(i) for i in tot])

    
def recherche_dicho(l,x):
    if len(l)==0:
        return False
    a=0
    b=len(l)-1
    while abs(b-a)>1:
        c=(a+b)//2
        if l[c]>x:
            b=c
        else:
            a=c
    return l[a]==x or l[b]==x

def recherche_ind_dicho(l,x):
    a=0
    b=len(l)-1
    if b<=0:
        return a
    while abs(b-a)>1:
        c=(a+b)//2
        if l[c]>x:
            b=c
        else:
            a=c
    if x>l[b]:
        return b
    return a

def inserer_dicho(l,x):
    ind=recherche_ind_dicho(l,x)
    return l[:ind+1]+[x]+l[ind+1:]
    
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
    

#Essayons d'une autre manière, celle-ci étant apparemment trop longue
#On peut calculer les sommes en les comptant avec l'ordre et en divisant par le nombre de permutations possibles. On raisonne alors par mémoïsation et récursivité
#Une telle méthode serait également trop longue cependant

#On peut donc plutôt raisonner ainsi: en stockant dans num des valeurs telles que num[i][j] représente le nombre de sommes pour atteindre i telles que le premier terme soit strictement supérieur à j (on représente toujours les sommes comme des suites croissantes) on a alors num[n][i]=sum([1+num[n-k][k-1] for k in range(i+1,n)])

#Déclarons et remplissons donc un tel tableau qui va jusqu'à n

def init_num(n):
    num=[]
    for k in range(n+1):
        num.append(n*[0])
    return num

def remplit_num(n):
    num=init_num(n)
    num[1][0]=0
    num[2][0]=1
    for i in range(3,n+1):
        for j in range(n):
            num[i][j]=sum([1+num[i-k][k-1] for k in range(j+1,i//2+1)])
    return num
            

