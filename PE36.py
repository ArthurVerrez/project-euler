#PE36
#09/07/2016
#872187

def binaire(n):
    r=''
    while n!= 0:
        r = str(n%2) + r
        n=(n-n%2)//2
    return r

def palin(n):
    return n==n[::-1]


def sum_dbp(n):
    s=0
    for i in range(1,n):
        if palin(str(i)) and palin(binaire(i)):
            s+=i
    return s
