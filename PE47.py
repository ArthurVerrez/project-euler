#PE47
#09/07/2016
#134043

def prime(n):
    if n==2:
        return True
    
    if n<2 or n%2==0:
        return False
    for i in range(3,int(n**(1/2))+1,2):
        if n%i == 0:
            return False
    return True

def is_good(n,m):
    for i in range(n,n+m):
        if len(p_fact(i,[])) != m:
            return (False,i)
    return True,0

def dist_p_fact(n):
    i=1
    good=is_good(i,n)
    while not good[0]:
        i = good[1]+1
        good=is_good(i,n)
    return i

def p_fact(n,a):
    if n==1:
        return a
    if prime(n):
        a.append(n)
        return a
    i=1
    if a!= []:
        i=a[-1]
    while i<int(n/2)+1:
        i+=1
        if n%i==0 and prime(i):
            a.append(i)
            break
        
    while n%i==0:
        n=n//i
    return p_fact(n,a)
