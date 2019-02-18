#PE55
#03/08/2016
#249

def pal(n):
    s=str(n)
    return s==s[::-1]

def lychrel(n):
    for i in range(50):
        s=str(n)
        n=n+int(str(n)[::-1])
        if pal(n):
            return False
    return True

def count_lyc(n):
    r=0
    for i in range(1,n+1):
        if lychrel(i):
            r+=1
    return r
