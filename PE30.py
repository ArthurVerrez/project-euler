#PE30
#20/07/2016
#443839

maxi=1000000

def is_good(n,p):
    s=str(n)
    r=0
    for i in s:
        r+= int(i)**p
    return r==n

def digit_f_p(p):
    r=0
    for i in range(2,maxi):
        if is_good(i,p):
            r+=i
    return r
