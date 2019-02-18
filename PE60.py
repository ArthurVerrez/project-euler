#PE60
#29/04/2017
#On trouve (8389, 6733, 5701, 5197, 13) donc 26033


#Taille du set que l'on recherche
W=4


#Remarquons tout d'abord qu'un set ne peut pas contenir deux fois le même nombre car 1 n'est pas premier et pour tout a>1 en concaténant 2 fois a, aa n'est pas premier

from numpy import *
#N est l'estimation du plus grand nombre dont on devra vérifier la primalité
N=100000000


#Applique la méthode du crible d'erathostène, era(n) renvoie une liste l telle que l[i] renvoie True si i est premier, False sinon et une autre liste primes qui est la liste des premiers
def era(n):
    l=(n+1)*[True]
    l[0]=False
    l[1]=False
    l2=[]
    for i in range(2,n+1):
        if l[i]:
            l2.append(i)
            for j in range(2*i,n+1,i):
                l[j]=False
    return l,l2

is_prime,primes=era(N)


#Vérifie si ab et ba (concaténation) sont premiers 
def conca_pr(a,b):
    return is_prime[int(str(a)+str(b))] and is_prime[int(str(b)+str(a))]

#Vérifie si un set convient
def convient(set):
    for i in range(len(set)):
        for j in range(i+1,len(set)):
            if not conca_pr(set[i],set[j]):
                return False
    return True

#Vérifie si le set d'indice a convient
def convient_ind(a):
    set=[primes[k] for k in a]
    return convient(set)


#On va chercher les W-uplets d'indices de somme minimale en approximant que ce sera pareil pour les nombres premiers correspondants
#ind[i] est la liste des W-uplets d'indices qui ont une somme égale à i



def next_1_ind(a):
    #l donne l'ensemble des ensemble d'indices ayant une somme plus 1 comparée à l'ancienne
    a[-1]+=1
    l=[a.copy()]
    a[-1]-=1
    for i in range(len(a)-1):
        if a[i]<a[i+1]-1:
            a[i]+=1
            l.append(a.copy())
            a[i]-=1
    return l

def next_ind(ind):
    a=[]
    for l in ind:
        for b in next_1_ind(l):
            if b not in a:
                a.append(b)
    return a

def answer():
    ind=[[k for k in range(W)]]
    i=0
    while True:
        for a in ind:
            if convient_ind(a):
                return a
        print(ind[0][-1])
        ind=next_ind(ind)
    
#Essayons une autre méthode moins à cheval sur la somme minimale et plus sur la recherche de la propriété en elle même

def answer_bis():
    for i in range(len(primes)):
        for j in range(i):
            if conca_pr(primes[i],primes[j]):
                for k in range(j):
                    if conca_pr(primes[j],primes[k]) and conca_pr(primes[i],primes[k]):
                        for l in range(k):
                            if conca_pr(primes[l],primes[k]) and conca_pr(primes[l],primes[i]) and conca_pr(primes[l],primes[j]):
                                for m in range(l):
                                    if conca_pr(primes[m],primes[l]) and conca_pr(primes[m],primes[k]) and conca_pr(primes[m],primes[j]) and conca_pr(primes[m],primes[i]):
                                        return primes[i],primes[j],primes[k],primes[l],primes[m]


