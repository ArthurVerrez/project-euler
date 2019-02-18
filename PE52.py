#PE52
#10/07/2016
#142857

#n et m sont des listes
def same_digits(n,m):
    if len(m)==0:
        return True
    if m[0] in n:
        n.remove(m[0])
        return same_digits(n,m[1::])
    return False

def is_good(n,m):
    for i in range(2,m+1):
        if not same_digits(list(str(n)),list(str(i*n))):
            return False
    return True

def permuted_mult(m):
    i=1
    while not is_good(i,m):
        i+=1
    return i
