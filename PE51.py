#PE51
#29/04/2017
#121313 for 120383,[1, 3, 5]

from numpy import *
#N est l'estimation du plus grand nombre dont on devra vérifier la primalité
N=1000000

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




#Donne l'ensemble des listes strictement croissantes de longueur s avec des éléments dans [|d,q|]  par mémoïsation, L[d,q,s] étant la liste voulue en considérant que d,q,s<10

NL=11
L=[]
for i in range(NL):
    l1=[]
    for j in range(NL):
        l2=[]
        for k in range(NL):
            l2.append([])
        l1.append(l2)
    L.append(l1)

            



def l_possible_aux(d,q,s):
    if s==1:
        return [[k] for k in range(d,q+1)]
    if len(L[d][q][s])>0:
        return L[d][q][s]
    
    tot=[]
    for i in range(d,q+1):
        poss=l_possible_aux(i+1,q,s-1)
        for l in poss:
            tot.append([i]+l)
    L[d][q][s]=tot
    return tot

def l_possible(q,s):
    return l_possible_aux(0,q,s)
    

#Takes an integer n and a list l of power of ten of n representing which digits to replace with a and the function returns how many newly created integer are primes
def count_n_l(n,l):
    c=0
    for a in range(1,10):
        if p_rep(a,n,l):
            c+=1
    if len(str(n))-1>max(l) and p_rep(0,n,l):
        c+=1
    return c


#Takes an integer a in [|0,9|], an integer n and a list l of power of ten of n representing which digits to replace with a, for example l=[1,2] and 2312 gives 2aa2. The function returns True if the given number is prime, False otherwise, assuming the list prime contains the information on the number we want to verify.
def p_rep(a,n,l):
    for i in l:
        n-=(n//10**i - (n//10**(i+1))*10)*10**i
        n+=a*10**i
    return is_prime[n]
    
    
#Takes an integer n and returns how many newly created integer are primes
def count_n(n):
    r=0
    q=len(str(n))-1
    for s in range(1,q+1):
        poss_l=l_possible(q,s)
        for l in poss_l:
            c=count_n_l(n,l)
            if c>r:
                r=c
    return r
    


#Gives the answer for 0<w<10 primes in a same family
def answer(w):
    i=0
    while count_n(primes[i])<w:
        i+=1
    return primes[i]
    


