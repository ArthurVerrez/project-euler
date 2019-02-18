#PE28
#07/07/2016
#669171001

from numpy import *

def spiral(n):
    x=1
    a=array([[1]])
    while x<n:
        if x%2 == 0:
            b=array([arange(x**2 + x, x**2, -1)])
            a=concatenate((b.T, a), axis=1)
            b=array([arange(x**2 + x + 1, (x+1)**2 + 1)])
            a=concatenate((b,a),axis=0)
        else:
            b= array([arange(x**2 + 1, x**2 + x + 1)])
            a = concatenate((a,b.T), axis=1)
            b= array([arange((x+1)**2, x**2 + x, -1)])
            a=concatenate((a,b), axis=0)
        x+=1
    return a

#Only works with n uneven
def spiral_diagonals(n):
    a=spiral(n)
    return sum(diag(a))+sum(diag(a[::-1,::])) -1
