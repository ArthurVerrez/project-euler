#PE41
#06/08/2016
#7652413

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


def prime(n):
    if n==2:
        return True
    
    if n<2 or n%2==0:
        return False
    for i in range(3,int(n**(1/2))+1,2):
        if n%i == 0:
            return False
    return True


#Réponse obtenue pour n=7
def larg_pan(n):
    p=permutations(list(range(1,n+1)))
    
    print("perm")
    
    for i in range(len(p)):
        p[i]=int("".join(str(j) for j in p[i]))
        
    print("replace")

    r=0
    for i in p:
        if i>r and prime(i):
            r=i
    return r
