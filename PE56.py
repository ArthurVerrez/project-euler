#PE56
#21/07/2016
#972


def digit_sum(n):
    a=str(n)
    s=0
    for i in a:
        s+=int(i)
    return s

def pds(n):
    m=0
    for a in range(100):
        for b in range(100):
            r=digit_sum(a**b)
            if r>m:
                m=r
    return m
