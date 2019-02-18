#PE27
#07/07/2016
#[71, -61, 971],-59231


def prime(n):
    if n==2:
        return True
    
    if n<2 or n%2==0:
        return False
    for i in range(3,int(n**(1/2))+1,2):
        if n%i == 0:
            return False
    return True

def num_of_primes(a,b):
    
    n=0
    while prime(n**2 + a*n + b):
        n+=1
    return n

def quadratic_primes(m):
    maxi=[0,0,0]
    for a in range(m):
        for b in range(m):
            for xa,xb in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                np=num_of_primes(xa*a,xb*b)
                if np > maxi[0]:
                    maxi=[np, xa*a,xb*b]
    return maxi
        
