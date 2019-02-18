#PE5
#04/07/2016
#232792560

def evenly_divisible_until(n,top):
    for i in range(1,top+1):
        if n%i != 0:
            return False
    return True

def smallest_multiple(n):
    i=n
    while not evenly_divisible_until(i,n):
        i+=n
    return i
