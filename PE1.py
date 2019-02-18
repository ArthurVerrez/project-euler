#PE1
#03/07/2016
#233168

def sum_multiples_of_3_and_5_below(n):
    s=0
    for i in range(n):
        if i%3==0 or i%5==0:
            s+=i
    return s
