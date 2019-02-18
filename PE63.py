#PE63
#23/04/2017
#49

#Il faut faire attention au fait qu'il puisse y avoir 2 fois le même nombre
tab=[]

#Renvoie le nombre de b tels que len(str(b**n))==n 
def n_digit(n):
    b=0
    r=0
    a=1
    while a<=n:
        b+=1
        a=len(str(b**n))
        if a==n:
            r+=1
            print(b**n)
    return r
            

#Pas satisfaisant mais ça a l'air de marcher, donne peut être la réponse pour m assez grand
def trouve(m):
    r=0
    for i in range(1,m):
        r+=n_digit(i)
    return r
