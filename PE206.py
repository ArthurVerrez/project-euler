#PE206
#31/07/2016
#1389019170

def is_good(n):
    s=str(n)
    if len(s) != 19:
        return False
    for i in range(1,10):
        if s[2*i - 2] != str(i):
            return False
    return s[-1] == '0'

def conc_sq():
    i=1010101010
    while not is_good(i**2):
        i+=10
        
    return i
