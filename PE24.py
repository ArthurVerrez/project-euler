#PE24
#08/07/2016
#[2, 7, 8, 3, 9, 1, 5, 4, 6, 0]

#perm ne contient pas x
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

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

def quicksort(t):
    if t==[]:
        return []
    up=[]
    down=[]
    for i in t[:len(t)-1]:
        if i>t[-1]:
            up.append(i)
        elif t[-1]>i:
            down.append(i)
    return quicksort(down)+[t[-1]]+quicksort(up)
