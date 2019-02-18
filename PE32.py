#PE32
#05/08/2016
#45228

def permutations_aux(x,perm):

    if len(x) == 2:
        perm.append(x)
        perm.append(x[::-1])
    else:
        for i in range(len(x)):
            y=x
            y[0],y[i]=y[i],y[0]
            perm_y=[]
        
            permutations_aux(y[1::],perm_y)
        
            for j in range(len(perm_y)):
                perm.append([y[0]]+perm_y[j])

def permutations(x):
    p=[]
    permutations_aux(x,p)
    return p


def is_pan_prod(a):
    n=len(a)
    r=[]
    s=''.join(str(i) for i in a)
    for i in range(1,n-2):
        for j in range(i+1,n-1):
                if int(s[0:i+1])*int(s[i+1:j+1])==int(s[j+1:]):
                    r.append(int(s[j+1:]))
    return r

def pan_prod(n):
    p=permutations(list(range(1,n+1)))
    r=[]
    for i in p:
        aux=is_pan_prod(i)
        for j in aux:
            if not j in r:
                r.append(j)
    return sum(r)
