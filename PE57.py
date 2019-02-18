#PE57
#23/04/2017
#153

#On représentera les fractions comme des 2-tuples, (a,b) avec a
#le numérateur et b le dénominateur

def aux_exp(n):
    if n==1:
        return (2,1)
    a,b=aux_exp(n-1)
    return (2*a+b,a)


#Donne la nième itération de l'expansion de 2**(1/2)
def expansion(n):
    a,b=aux_exp(n)
    return (a+b,a)
    
#On pourrait essayer une méthode avec mémoïsation dans un tableau
#mais essayer tout d'abord une méthode plus brute

def more_digits(t):
    a=t[0]
    b=t[1]
    return len(str(a))>len(str(b))

#Donne le résultat
def count_digits(n=1000):
    c=0
    for i in range(1,n+1):
        if more_digits(expansion(i)):
            c+=1
    return c

#Il semblerait que cette méthode brute fait trop d'appels récursifs
#Essayons une méthode avec de la mémoïsation



def count_digits_m(n=1000):
    tab=1001*[(0,0)]
    def aux_exp_m(n):
        if n==1:
            return (2,1)
        if tab[n][1]>0:
            return tab[n]
        a,b=aux_exp_m(n-1)
        tab[n]=(2*a+b,a)
        return (2*a+b,a)
    
    def expansion_m(n):
        a,b=aux_exp_m(n)
        return (a+b,a)
        
    c=0
    for i in range(1,n+1):
        if more_digits(expansion_m(i)):
            c+=1
    return c
    