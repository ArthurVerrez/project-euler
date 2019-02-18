#PE2
#03/07/2016
#4613732

def sum_even_fibo_under(n):
    s = 0
    f1 = 1
    f2 = 2
    while f1 <= n:
        if f1%2 == 0:
            s+=f1
        f1,f2=f2,f1+f2
    return s
