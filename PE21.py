#PE21
#06/07/2016
#31626

def sum_amicable_under(top):

    div = [-1 for k in range(top+1)]
    
    def amicable(n,m):
        def proper_divisors(num):
            d=[1]
            for i in range(2, int(num/2)+1):
                if num%i == 0:
                    d.append(i)
            return d

        if div[n]==-1:
            div[n]=sum(proper_divisors(n))
        if div[m]==-1:
            div[m]=sum(proper_divisors(m))
        
        if n != m and div[n]== m and div[m]== n:
            return True

        return False


    s=0
    for i in range(2,top+1):
        for j in range(1,i):
            if amicable(i,j):
                s+= i+j
    return s
