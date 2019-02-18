#PE45
#15/07/2016
#1533776805

#Very long but works

def triangular(x):
    x*=2
    for n in range(1,int(x**(1/2))+1):
        if n*(n+1)==x:
            return True
    return False

def pentagonal(x):
    x*=2
    for n in range(1,int(x**(1/2))+1):
        if n*(3*n-1)==x:
            return True
    return False

def hexagonal(x):
    for n in range(1,int(x**(1/2))+1):
        if n*(2*n-1)==x:
            return True
    return False

#On trouve le prochain hexagonal et on vérifie les autres
def next_num(num,n_hex):
    i=num+4*n_hex+1
    n_hex+=1
    while not (triangular(i) and pentagonal(i)):
        i+=4*n_hex+1
        n_hex+=1
    return i
