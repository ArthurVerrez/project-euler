#PE53
#12/07/2016
#4075

import numpy as np



def combi_select(top,gr_th):
    c=np.zeros((top+1,top+1))

    def combi(n,k):
        if k>n:
            return 0
        if k==0:
            return 1
        if c[n,k] == 0:
            c[n,k] = (n*combi(n-1,k-1)//k)
        
        return c[n,k]

    r=0
    for i in range(1,top+1):
        for j in range(i+1):
            if combi(i,j)> gr_th:
                r+=1
    return r
    
    
