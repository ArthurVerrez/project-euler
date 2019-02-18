#PE10
#04/07/2016
#142913828922

def euclide(n):
    e=[True for k in range(n)]
    e[0]=False
    e[1]=False
    r=[]
    for i in range(2,n):
        if e[i]:
            r.append(i)
            for j in range(2*i, n, i):
                e[j] = False
    return r

def summation_of_primes(n):
    return sum(euclide(n))
