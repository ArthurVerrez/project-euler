#PE34
#15/07/2016
#40730


def fact(n):
    r=1
    for i in range(2,n+1):
        r*=i
    return r

def is_equal(n):
    s=str(n)
    r=0
    for i in s:
        r+=fact(int(i))
    return r==n


#Testé avec 1000000
def digit_fact(n):
    r=0
    for i in range(10,n):
        if is_equal(i):
            r+=i
    return r
