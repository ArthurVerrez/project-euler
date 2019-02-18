#PE65
#01/05/2017
#272


#If l represents a continued fraction, this function returns the resulting fraction as a tuple
def cont_fra(l):
    if len(l)==1:
        return (l[0],1)
    (a,b)=cont_fra(l[1:])
    return (l[0]*a+b,a)

#Gives a list representing the continued fraction of e until the nth term for n>=1
def cont_fra_e(n):
    l=n*[1]
    l[0]=2
    for i in range(2,n,3):
        l[i]=(i+1)*2//3
    return l

def answer(n=10):
    (a,b)=cont_fra(cont_fra_e(n))
    return sum([int(k) for k in str(a)])
        