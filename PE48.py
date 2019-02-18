#PE48
#15/07/2016
#9110846700

def self_powers(n):
    total=0
    for i in range(1,n+1):
        total+=i**i
    return total
