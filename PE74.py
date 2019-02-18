#PE74
#01/05/2017
#402

#Tout d'abord une définition récursive de la factorielle
def rec_fact(n):
    if n==0:
        return 1
    return n*rec_fact(n-1)

#Contient les factoriels de 0 à 9
fact=[rec_fact(k) for k in range(10)]

#Donne le prochain élement dans la chaîne de factoriels
def next_fact(n):
    return sum([fact[int(k)] for k in str(n)])

def length_fact_suit(n):
    l=[n]
    a=next_fact(n)
    while not a in l:
        l.append(a)
        a=next_fact(a)
    return len(l)

def answer(n=1000000):
    c=0
    for i in range(n+1):
        if length_fact_suit(i)==60:
            c+=1
    return c
        