#PE92
#23/04/2017
#8581146

#Donne le nombre suivant
def next_num(n):
    a=str(n)
    l=[]
    for i in a:
        l.append(int(i))
    s=0
    for i in l:
        s+=i**2
    return s
    
#Renvoie 89 ou 1 en fonction de la fin de la chaîne de n
def last_one(n):
    r=n
    while r!=1 and r!=89:
        r=next_num(r)
    return r

#Raisonnons par mémoïsation sur une liste l de 10**7 éléments qui contient à l[n] 1 ou 89 en fonction de si le nombre n arrive à la fin de sa chaîne à 1 ou 89

def init_tab_and_count(n=10000000):
    l=(n+1)*[0]
    l[1]=1
    l[89]=89
    s=0
    def aux(i):
        if l[i]>0:
            return l[i]
        r=aux(next_num(i))
        l[i]=r
        return r
    for i in range(1,len(l)-1):
        if l[i]==0:
            aux(i)
    for i in l:
        if i==89:
            s+=1
    return s

    
    