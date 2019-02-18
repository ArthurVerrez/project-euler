#PE46
#06/07/2016
#5777

p=[False,False,True]

def prime(n):
    if n==2:
        return True
    if n<2 or n%2==0:
        return False
    
    for i in range(3,int(n**(1/2))+1,2):
        if n%i == 0:
            return False
    
    add_to_prime(n)
    return True

def add_to_prime(n):
    for i in range(len(p), n):
        p.append(False)
    p.append(True)

def goldbach(n):
    for i in range(2,n):
        if (len(p)> i and p[i]) or prime(i):
            for j in range(1,int(n/2)):
                if n == i + 2*(j**2):
                    return True
    return False

def goldbach_limit():
    i=9
    while goldbach(i):
        i+=1
        while i%2 == 0 or ((len(p)> i and p[i]) or prime(i)):
            i+=1
    return i


