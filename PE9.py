#PE9
#04/07/2016
#(200, 375, 425), 31875000

def special_pythagorean_triplet(n):
    for c in range(2,n+1):
        for b in range(1,c):
            for a in range(b):
                if a**2+b**2==c**2 and a+b+c==n:
                    return (a,b,c),a*b*c
