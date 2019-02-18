#PE97
#22/04/2017
#8739992577


#Il suffit de déterminer les six premiers digits car 28433 > 10**4
#Pour ce faire, on peut remarquer que les unités, dizaines, centaines...
#des puissances de 2 présentent un pattern à partir d'un certain rang
#Il suffit donc de déterminer le pattern pour chaque puissance de 10


#Vérifie si un motif est bien un motif d'une liste donnée
#avec n vérifications
def verif_pattern(l,pat,n):
    m=len(pat)
    for i in range(n):
        if l[i*m:i*m+m] != pat:
            return False
    return True



#Prend une liste, une taille maximale de pattern et un nombre de
#vérification de pattern à faire et renvoie la liste du pattern
def find_pattern(l,maxi,n):
    for long in range(1,maxi):
        if verif_pattern(l,l[:long],n):
            return l[:long]

#Renvoie une liste de n nombres des parties 10**r des puissances de 2
#à partir de 2**k
def puiss_2(n,r,k):
    l=[]
    a=2**k
    for i in range(n):
        l.append((a%(10**(r+1))-a%(10**(r)))//(10**r))
        a*=2
    return l

#Renvoie les patterns des unités, dizaines.... jusqu'à 10**5
#des puissances de 2
def patterns():
    pat=[]
    for i in range(6):
        l=puiss_2(100000,i,40)
        pat.append(find_pattern(l,30000,3))
    return pat

#pats=patterns()

#Donne les 5 derniers digits de 2**k
def last_dig(k):
    dig=[]
    for i in range(6):
        a=(k-40)%len(pats[i])
        dig.append(pats[i][a])
    return dig

#Il suffit alors de multiplier le résultat par 28433 et d'ajouter 1


#La technique précédente étant bien trop stupide et tout
#bonnement fausse, on raisonnera tout simplement modulo 10**10

def dern_dig(k):
    a=1
    for i in range(k):
        a*=2
        a=a%(10**10)
    return a

