#PE20
#06/07/2016
#648

def fact(n):
    if n==1:
        return n
    return n*fact(n-1)

def count_num_fact(n):
    s=0
    for k in list(str(fact(n))):
        s+=int(k)
    return s
