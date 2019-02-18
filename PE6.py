#PE6
#04/07/2016
#25164150

def sum_square_difference(n):
    return sum(range(n+1))**2 - sum([k**2 for k in range(n+1)])
