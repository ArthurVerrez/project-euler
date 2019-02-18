#PE38
#06/08/2016
#932718654

def pan(s):
    if len(s) != 9:
        return False
    r=[False for k in range(10)]
    r[0]=True
    for i in s:
        if r[int(i)]:
            return False
        r[int(i)]=True
    return not False in r

#Pas totalement rigoureux, il faudrait vérifier jusqu'à len(aux)< 10
def concat_pan(n):
    i=1
    aux=""
    while len(aux)<9:
        aux+=str(i*n)
        i+=1
    if pan(aux):
        return int(aux)
    return 0

def max_concat_pan():
    r=0
    #Valeur un peu prise au hasard
    for k in range(1,100000):
        aux=concat_pan(k)
        if aux>k:
            r=aux
    return r

