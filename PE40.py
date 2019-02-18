#PE40
#21/07/2016
#210

def champ_const(n):
    a=0
    r=""
    m=1
    while a<n:
        r+=str(m)
        a+=len(str(m))
        m+=1
    return r

def answer():
    r=1
    a=champ_const(1000000)
    for i in range(7):
        r*=int(a[10**i - 1])
    return r
