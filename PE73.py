#PE73
#02/05/2017
#7295372





#On va essayer de lister toutes les possibilités de fractions dans un ordre quelconque, les réduire à une fraction irréductible puis les trier.
#On représente les fractions par des tuples (a,b)

#Liste les fractions a/b (=(a,b)) telles que 1<b<=d et 1<=a<b
def list_fract_between(d,m=1/3,M=1/2):
    l=[]
    for b in range(2,d+1):
        for a in range(int(m*b),int(M*b)+1):
            
            l.append(irred((a,b)))
    return l


#Prend une fraction (a,b) et renvoie la fraction irréductible correspondante (c,d)
#Pour ce faire, on a besoin de calculer le pgcd de a et b
#On va donc calculer l'ensemble des diviseurs premiers de a et b

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

#div_p=era(N+1)

#Renvoie le plus grand élément dans deux listes triées et 1 sinon
def pgec(l1,l2):
    for i in l1[::-1]:
        for j in l2[::-1]:
            if i==j:
                return i
    return 1

def pgcd(a,b):
    p=pgec(div_p[a],div_p[b])
    if p==1:
        return 1
    else:
        return p*pgcd(a//p,b//p)
        
def euclide(a,b):
    if a==0:
        return b
    q=b//a
    r=b-q*a
    return euclide(r,a)
    
def irred(fraction):
    a=fraction[0]
    b=fraction[1]
    p=euclide(a,b)
    return (a//p,b//p)

#Fusionne deux listes de fractions sans rajouter les doublons
def fusion(a,b):
    l=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        
        if (a[i][0]/a[i][1])<(b[j][0]/b[j][1]):
            if len(l)==0 or l[-1]!=a[i]:
                l.append(a[i])
            i+=1
        else:
            if len(l)==0 or l[-1]!=b[j]:
                l.append(b[j])
            j+=1
    if i>=len(a):
        l+=b[j::]
    else:
        l+=a[i::]
    return l
        

def tri_fract(l):
    if len(l)<=1:
        return l
    else:
        return fusion(tri_fract(l[:len(l)//2]),tri_fract(l[len(l)//2:]))


#Pas satisfaisant moralement, mais marche au bout de beaucoup de temps
def answer(a):
    l=tri_fract(a)
    i=0
    while l[i]!=(1,3):
        i+=1
    j=0
    while l[j]!=(1,2)
    return len(l[i+1:j])

        
    
    
