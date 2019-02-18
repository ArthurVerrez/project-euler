#PE23
#08/07/2016
#4179871

def divisors(n):
    d=[1]
    if n<=1:
        return d
    
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            d.append(i)
    return d

def abundant(n):
    return sum(divisors(n))>n

def list_ab(n):
    r=[]
    for i in range(1,n):
        if abundant(i):
            r.append(i)
    return r

def non_ab_sum(n):
    a=list_ab(n)
    print("Etape 1")

    can_be=n*[False]
    for i in a:
        for j in a:
            if i+j <= n:
                can_be[i+j-1]=True
    r=0
    for i in range(n):
        if not can_be[i]:
            r+=i+1
    
    return r


        
        
