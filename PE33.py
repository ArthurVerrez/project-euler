#PE33
#05/08/2016
#100

def is_good(t):
    a=list(str(t[0]))
    b=list(str(t[1]))
    if a[0] != '0' and a[0] in b:
        b2=b.copy()
        b2.remove(a[0])
        if b2[0] != '0' and int(a[1])/int(b2[0])==t[0]/t[1]:
            return True
    if a[1] != '0' and a[1] in b:
        b2=b.copy()
        b2.remove(a[1])
        if b2[0] != '0' and int(a[0])/int(b2[0])==t[0]/t[1]:
            return True
    return False
    

def dcf():
    r=[]
    for i in range(10,100):
        for j in range(i+1,100):
            if is_good((i,j)):
                r.append((i,j))
    return r

def reduce(t):
    a=t[0]
    b=t[1]
    for i in range(a,2,-1):
        if a%i == 0 and b%i == 0:
            a=a//i
            b=b//i
    return (a,b)
