#PE357
#03/05/2017

def is_prime(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def crible(n):
    a=[True for k in range(n)]
    if(len(a)>0):
        a[0]=False
    if(len(a)>1):
        a[1]=False
    i=2
    while(i<len(a)):
        if(a[i]):
            for k in range(2*i, len(a), i):
                a[k]=False
        i+=1
    p=[]
    for k in range(len(a)):
        if(a[k]):
            p.append(k)
    return a,p

N=10000
is_prime,primes =crible(N)



def harshad(n):
    a=list(str(n))
    a=[int(a[k]) for k in range(len(a))]
    return n%sum(a)==0

def strong_harshad(n):
    a=list(str(n))
    a=[int(a[k]) for k in range(len(a))]
    s=sum(a)
    if(n%s!=0):
        return False
    return is_prime[n//s]

def srthp(n):
    if(not is_prime[n]):
        return False
    a=list(str(n))
    a=[int(a[k]) for k in range(len(a))]
    s=sum(a[:-1])
    return ((n-a[-1])//10)%s!=0
