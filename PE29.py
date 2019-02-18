#PE29
#08/07/2016
#9183

def dist_powers(n):
    r=[]
    for a in range(2,n+1):
        for b in range(2,n+1):
            aux=a**b
            if aux not in r:
                r.append(aux)
    return len(r)
