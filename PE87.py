#PE87
#01/02/19
#réponse: 1097343 (après longtemps)
#On fait d'abord un crible d'eratosthène pour trouver tous les nombres premiers en dessous d'un n donné


#Renvoie une liste avec croissante avec tous les nombres premiers jusqu'à n exclu
#Non performant
def crible(n):
    a=[True for k in range(n)]
    if(len(a)>0):
        a[0]=False
    if(len(a)>1):
        a[1]=False
    i=2
    while(i<len(a)):
        if(a[i]):
            for k in range(2*i, len(a), i):
                a[k]=False
        i+=1
    p=[]
    for k in range(len(a)):
        if(a[k]):
            p.append(k)
    return p


#Returns a list without duplicates of all the numbers under n that can be expressed as a power triple of prime numbers
def set_power_triples(n):
    p=crible(int((n)**(1/2)))
    s=set()
    for i in range(len(p)):
        for j in range(i, len(p)):
            for k in range(j, len(p)):
                a=p[i]
                b=p[j]
                c=p[k]
                for w in [(a,b,c),(a,c,b),(b,a,c),(b,c,a),(c,a,b),(c,b,a)]:
                    z=w[0]**2+w[1]**3+w[2]**4
                    if(z<=n):
                        s.add(z)
    return list(s)

def calculus(n):
    return len(set_power_triples(n))
def answer():
    N=50000000
    return calculus(N)
