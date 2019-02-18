#PE25
#08/07/2016
#4782

def digit_fibo(n):
    i=1
    fi=1
    fj=1
    while fi < 10**(n-1):
        fi,fj=fj,fi+fj
        i+=1
        
    return i
