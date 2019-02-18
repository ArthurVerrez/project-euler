#PE85
#02/05/2017
#(36, 77) et 36*77=2772

#On va raisonner avec des triangles dont on va augmenter la taille
#On représentera un rectangle par un tuple (a,b) avec a la largeur et b la longueur
#Ecrivons tout d'abord une fonction qui pour une surface données donne le nombre de rectangles


#Donne le nombre de rectangles c,d dans un rectangle a,b (on considère c<=a et d<=b
def rect_in_rect(a,b,c,d):
    #En largeur
    larg=a-c+1
    #En longueur
    long=b-d+1
    return larg*long


def num_rect(a,b):
    r=0
    for c in range(1,a+1):
        for d in range(1,b+1):
            r+=rect_in_rect(a,b,c,d)
    return r

def tab_val(n):
    l=n*[0]
    for i in range(n):
        l[i]=n*[0]
    for i in range(n):
        for j in range(n):
            l[i][j]=num_rect(i,j)
    return l

#En appelant tab_val(100) on réalise qu'on arrive vite à 2 millions
#Le but est maintenant de trouver les couples d'indices qui réalisent le mieux la condition

def answer(l,N=2000000):
    a=0
    b=0
    for i in range(len(l)):
        for j in range(len(l)):
            if abs(l[i][j]-N)<abs(l[a][b]-N):
                a=i
                b=j
    return a,b
    
    
    