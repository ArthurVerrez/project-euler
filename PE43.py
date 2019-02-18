#PE43
#06/08/2016
#16695334890

div=[2,3,5,7,11,13,17]

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

def div_pan(s):
    for i in range(1,8):
        if not int(s[i:i+3])%div[i-1]==0:
            return False
    return True

def sum_pan():
    p=permutations(list(range(10)))
    print("perm")

    for i in range(len(p)):
        p[i]="".join(str(j) for j in p[i])

    print("replace")

    s=0
    for i in p:
        if div_pan(i):
            s+=int(i)
    return s
