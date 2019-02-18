#PE49
#07/07/2016
#(2969, 6299, 9629)


#Si on part avec des nombres, il faut mettre en argument list(str(n))
def are_perm(n,m):
    if len(n) == 0:
        return True
    
    if n[0] in m:
        m.remove(n[0])
        return are_perm(n[1::],m)
    return False

def prime(n):
    if n==2:
        return True
    
    if n<2 or n%2==0:
        return False
    for i in range(3,int(n**(1/2))+1,2):
        if n%i == 0:
            return False
    return True

def is_good(i,r):
    return are_perm(list(str(i)), list(str(i+r))) and are_perm(list(str(i)), list(str(i+2*r))) and prime(i+r) and prime(i+2*r) and (i != 1487 or r!=3330)

def prime_perm():
    for i in range(1000, 10000):
        if prime(i):
            for r in range(1, int((10000-i)/2)):
                if is_good(i,r):
                    return (i, i+r, i+2*r)
                
                        

