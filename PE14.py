#PE14
#04/07/2016
#[837799, 524]

def longest_collatz_under(n):
    collatz=[0 for i in range(n)]

    def collatz_length(m):
        k=m
        c=0
        while k != 1:
            if k<m and collatz[k]!=0:
                collatz[m]=c+collatz[k]
                return collatz[m]
            c+=1
            if k%2 == 0:
                k=int(k/2)
            else:
                k=3*k+1
        return c
    
    maxi=[0,0]
    for i in range(1,n):
        c=collatz_length(i)
        if c>maxi[1]:
            maxi[0]=i
            maxi[1]=c
    return maxi
