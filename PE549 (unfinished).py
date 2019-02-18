#PE549
#31/07/2016

f=[1,1]

def fact(n,f):
    if len(f) <= n:
        f+=(n-len(f)+1)*[0]
    if f[n]==0:
        f[n]=fact(n-1,f)*n
    return f[n]

def small(n):
    i=1
    while fact(i,f)%n:
        i+=1
    return i

def somme(n):
    s=0
    for i in range(2,n+1):
        s+=small(i)
    return s
