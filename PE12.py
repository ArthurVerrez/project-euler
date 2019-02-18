#PE12
#04/07/2016
#76576500

def div_aux(n,d,m):
    if n==1:
        return d
    
    m+=1
    while m <= n:
        if n%m==0:
            break
        m+=1
    a=0
    while n%m==0:
        a+=1
        n=n//m
    d*=(a+1)
    return div_aux(n,d,m)

def div(n):
    return div_aux(n,1,1)


def triangle_number_divisors(n):
    i=1
    add=2
    while div(i)<n:
        i+=add
        add+=1
    return i
