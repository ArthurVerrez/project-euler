#PE69
#29/04/2017
#510510

#L'expression de l'indicatrice d'Euler permet de ramener la recherche de phi(n) à la recherche des nombres premiers qui divisent n


#On raisonne de manière similaire au crible d'erathostène pour déterminer les nombres premiers qui divisent n

#Era renvoie une liste telle que l[m] contient l'ensemble des nombres premiers divisant n
def era(n):
    p=n*[True]
    p[0]=False
    p[1]=False
    l=[]
    for k in range(n):
        l.append([])
        
    for i in range(2,n):
        if p[i]:
            for j in range(i,n,i):
                l[j].append(i)
                p[j]=False
    return l

N=1000000
div_p=era(N+1)


def n_sur_phi(n):
    p=1
    for k in div_p[n]:
        p*=k/(k-1)
    return p

def answer():
    m=0
    n=0
    for i in range(1,N+1):
        a=n_sur_phi(i)
        if a>m:
            n=i
            m=a
    return n