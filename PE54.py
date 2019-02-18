#PE54
#24/04/2017
#376

f=open("C:/Users/Arthur/Google Drive/Projets/Programmation/Project Euler/PE54_hands.txt","r")

order=['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suit=['D','S','C','H']

def card_num(a):
    for i in range(len(order)):
        if a==order[i]:
            return i
def suit_num(a):
    for i in range(len(order)):
        if a==suit[i]:
            return i

hands=f.readlines()
p1=[]
p2=[]
for s in hands:
    l=[]
    for i in range(0,30,3):
        a=s[i:i+2]
        l.append((card_num(a[0]),suit_num(a[1])))
        
    p1.append(sorted(l[:5]))
    p2.append(sorted(l[5:]))

#Renvoie True si la main est un flush et l'indice de la plus grande carte
def F(h):
    s=h[0][1]
    for i in range(1,5):
        if h[i][1]!=s:
            return False,0
    return (True,[h[k][0] for k in range(4,-1,-1)])


def suite_as(h):
    return [h[k][0] for k in range(5)]==[0,1,2,3,12]

#Renvoie True si les cartes sont consécutives et i l'indice du premier
#Il faut faire attention et également vérifier le cas AS,2,3...
def S(h):
    if suite_as(h):
        return True,-1
    i=h[0][0]
    for j in range(1,5):
        if h[j][0]!=i+j:
            return False,0
    return (True,i)
        
#Renvoie True si h est une royale flush
def RF(h):
    #Si le premier n'est pas un 10, ce n'est pas un RF
    if h[0][0]!=8:
        return False,0
    if not SF(h)[0]:
        return False,0
    return True,0

#Straight Flush, retourne Bool,i,j avec i l'indice du premier et j la couleur
def SF(h):
    f=F(h)
    if not f[0]:
        return (False,0,0)
    s=S(h)
    if not s[0]:
        return (False,0,0)
    
    return (True,f[1],s[1])

def num_same_kind(h):
    r=13*[0]
    for i in h:
        r[i[0]]+=1
    return maximum(r)

#Full House, si h contient déjà 3 éléments d'un type i
def FH(h,i):
    r=[]
    for j in h:
        if j[0]!=i:
            r.append(j[0])
    if r[0]==r[1]:
        return (True,(i,r[0]))
    else:
        return False,0

#Renvoie le maximum d'une liste et l'indice du max
def maximum(r):
    m=(r[0],0)
    for i in range(1,len(r)):
        if r[i]>m[0]:
            m=(r[i],i)
    return m

#Renvoie l'indice de la première occurence de i dans r
def ind(r,a):
    for i in range(len(r)):
        if r[i]==a:
            return i
        
#Renvoie True si h contient une paire et i,j avec i<j les indices dans la liste l
def pair(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if j != i and l[i]==l[j]:
                if i<j:
                 return True,i,j
                return True,j,i
    return False,0,0
    

#Renvoie True,(i,j,k) si h contient 2 paires avec i>j l'indice des paires et k l'indice de la dernière carte en considérant que h contient au moins une paire
def two_pairs(h):
    l=[h[k][0] for k in range(5)]
    p,i,j=pair(l)
    if not p:
        return False,0
    pair1=l[i]
    del(l[j])
    del(l[i])
    p,i,j=pair(l)
    if not p:
        return False,0
    pair2=l[i]
    del(l[j])
    del(l[i])
    if pair1>pair2:
        return True,(pair1,pair2,l[0])
    return True,[pair2,pair1,l[0]]
    
#0 Highest card
#1 1 paire
#2 2 paires
#3 three of a kind
#4 Straight
#5 Flush
#6 Full House
#7 Four of a kind
#8 Straight Flush
#9 Royal Flush


#Le deuxième éléments sert en cas d'égalité, pour le full house, il y a deux éléments à comparer, on utilisera l'ordre lexicographique
def which_hand(h):
    rf=RF(h)
    if rf[0]:
        return (9,0)
    sf=SF(h)
    if sf[0]:
        if sf[2]==-1:
            return (8,sf[1][1:]+[-1])
        return (8,sf[1])
    n,i=num_same_kind(h)
    if n==4:
        return (7,i)
    if n==3:
        fh=FH(h,i)
        if fh[0]:
            return (6,fh[1])
    f=F(h)
    if f[0]:
        return (5,f[1])
    s=S(h)
    if s[0]:
        return (4,s[1])
    if n==3:
        l=[h[k][0] for k in range(5)]
        for k in range(3):
            del(l[ind(l,i)])
        return (3, l[::-1])
    if n==2:
        tp=two_pairs(h)
        if tp[0]:
            return 2,tp[1]
        p,i,j=pair([h[k][0] for k in range(5)])
        if p:
            l=[h[k][0] for k in range(5)]
            del(l[j])
            del(l[i])
            return (1,h[i][0],l[::-1])
    return (0,[h[k][0] for k in range(4,-1,-1)])
        
        
    
#Renvoie 1 si la main h1 gagne, 2 si la main h2 gagne
def one_win_hand(h1,h2):
    return which_hand(h1)>which_hand(h2)

def count_one_win():
    r=0
    for i in range(len(p1)):
        if one_win_hand(p1[i],p2[i]):
            r+=1
    return r