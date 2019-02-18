#PE39
#31/07/2016
#840

def values(p):
    v=[]
    cprior=0
    for a in range(1,p-1):
        for b in range(1,a):
            c=p-a-b
            if c > 0 and b != cprior and a**2 == b**2 + c**2:
                v.append([a,b,c])
                cprior = c
    return v

def integer_right_tr(n):
    m=[0,0]
    for p in range(1,n+1):
        print(p)
        long=len(values(p))
        if long > m[0]:
            m=long,p
    return m[1]
