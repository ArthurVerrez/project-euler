#PE35
#21/07/2016
#55


def euclide(n):
    e=[True for k in range(n)]
    e[0]=False
    e[1]=False
    for i in range(2,n):
        if e[i]:
            for j in range(2*i, n, i):
                e[j] = False
    return e

def con_circ_p(n):
    r=0
    euc=euclide(n)

    def rot_prime(n):
        a=str(n)
        for i in range(len(a)):
            if not euc[int(a[i:]+a[:i])]:
                return False
        return True

    for i in range(n):
        if rot_prime(i):
            r+=1
    return r
    
