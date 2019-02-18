#PE58
#23/04/2017
#26241


#Renvoie True si un nombre est premier, False sinon
def prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**(1/2))+1,2):
        if n%i==0:
            return False
    return True


#Donne le résultat demandé, à l'intérieur de la fonction, p donne le nombre de nombres premiers dans r
def larg_sup(b=0.1):
    r=[1]
    p=0
    n=1
    while p/len(r) > b or n<7:
        
        n+=2
        for i in range(r[-1]+1+n-2,r[-1]+1+4*n-4,n-1):
            r.append(i)
            if prime(i):
                p+=1
    return n
    
