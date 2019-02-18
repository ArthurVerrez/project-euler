#PE7
#04/07/2016
#104743

def prime(n):
    if n==2:
        return True
    if n<2 or n%2==0:
        return False
    for i in range(3,int(n**(1/2))+1,2):
        if n%i == 0:
            return False
    return True

def n_th_prime(n):

    i=0
    j=0
    while i<n:
        j+=1
        while not prime(j):
            j+=1
        i+=1
    return j
