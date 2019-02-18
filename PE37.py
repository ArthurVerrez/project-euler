#PE37
#09/07/2016
#748317

def prime(n):
    if n==2:
        return True
    
    if n<2 or n%2==0:
        return False
    for i in range(3,int(n**(1/2))+1,2):
        if n%i == 0:
            return False
    return True

def trunc_prim_left_right(n):
    i=len(str(n))
    for j in range(1,i+1):
        if not (prime(n%(10**j)) and prime(n//10**(j-1))):
            return False
    return True

def sum_trunc_primes():
    s=0
    r=0
    i=10
    while r<11:
        if trunc_prim_left_right(i):
            print(i)
            s+=i
            r+=1
        i+=1
    return s
