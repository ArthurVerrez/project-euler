#PE62
#01/05/2017
#[5027, 7061, 7202, 8288, 8384] donc 5027**3=127035954683


#L'idée est de calculer les cubes 1 à 1, mettre le résultat dans une liste, les éléments seront réprésentés par des listes, et on trie les cubes dans l'ordre, donc on peut les insérer et les rechercher par dichotomie


#l doit être triée pour cette recherche dichotomique
def rech_dicho(l,x):
    a=0
    b=len(l)-1
    while abs(b-a)>1:
        c=(a+b)//2
        if l[c]>x:
            b=c
        else:
            a=c
    if l[a]==x or l[b]==x:
        return True
    return False

#Renvoie une liste triée qui contient l'élement x
def inser_dicho(l,x):
    if l==[]:
        return [x]
    a=0
    b=len(l)
    while abs(b-a)>1:
        c=(a+b)//2
        if l[c]>x:
            b=c
        else:
            a=c
    if l[a]>=x:
        return l[:a]+[x]+l[a:]
    #Si on arrive ici, on a l[b]>x
    return l[:b]+[x]+l[b:]


#Liste les cubes dans une liste l jusqu'à n**3 en les représentant par des listes triées m, on aura alors seulement une permutation du résultat que l'on veut
def list_cube(n):
    l=[]
    for i in range(n+1):
        l=inser_dicho(l,(sorted([int(k) for k in str(i**3)]),i))
    return l

#Trouve l'élément dont la première composante a le plus d'itérations dans une liste, renvoie alors la liste comprenant la liste des secondes composantes des itérations en question elt et son nombre d'occurences occ
def count_max(l):
    max_elt=[]
    #Indice de la première apparition de last_elt
    i0=0
    i=1
    last_elt=l[0][0]
    list_last_elt=[l[0][1]]
    while i<len(l):
        if l[i][0]!=last_elt:
            if len(max_elt)<len(list_last_elt):
                max_elt=list_last_elt.copy()
            last_elt=l[i][0]
            list_last_elt=[l[i][1]]
        else:
            list_last_elt.append(l[i][1])
            
        i+=1
    if len(max_elt)<len(list_last_elt):
        return list_last_elt
    return max_elt

def answer_perm(n):
    return count_max(list_cube(n))

#Il suffit alors d'appeler answer_perm(10000)
    
