#PE16
#06/07/2016
#1366

def power_digit_sum(n,m):
    s=0
    for k in list(str(n**m)):
        s+=int(k)
    return s
