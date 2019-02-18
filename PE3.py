#PE3
#03/07/2016
#6857

def prime(n):
    if n==2:
        return True
    
    if n<2 or n%2==0:
        return False
    for i in range(3,int(n**(1/2))+1,2):
        if n%i == 0:
            return False
    return True

def largest_prime_factor(n):
    if prime(n):
        return n
    for i in range(int(n**(1/2))+1, 1, -1):
        if n%i == 0 and prime(i):
            return i
    return 2
