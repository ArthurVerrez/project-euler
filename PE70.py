#PE70
#04/05/2017
#8319823

#On vole les fonctions qui permettent de calculer rapidement phi dans PE69

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

N=10000000
div_p=era(N+1)


def phi(n):
    p=n
    for k in div_p[n]:
        p=(p-p/k)
    return int(p)

#Renvoie l'indice d'un élement x dans une liste l
def indice(l,x):
    for i in range(len(l)):
        if l[i]==x:
            return i
    return -1

def are_perm(a,b):
    a=list(str(a))
    b=list(str(b))
    if len(a)!=len(b):
        return False
    for x in a:
        i=indice(b,x)
        if i==-1:
            return False
        del(b[i])
    return True

def list_phiperm():
    l=[]
    for i in range(1,N):
        p=phi(i)
        if are_perm(i,p):
            l.append((i,p))
    return l

def answer():
    l=list_phiperm()
    n=l[1][0]
    m=l[1][0]/l[1][1]
    for (i,p) in l[1:]:
        if i/p<m:
            n=i
            m=i/p
    return n


    