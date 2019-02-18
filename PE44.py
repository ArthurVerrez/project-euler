#PE44
#22/04/2017
#distance = 5482660 pour P(2167) - P(1020)


#renvoie le nième nombre pentagonal
def P(n):
    return n*(3*n-1)//2
    
#Renvoie Pi,Pj (i>j) tels que la Pn+Pm=Pi et Pn-Pm=Pj (il faut n>m)
#Renvoie False s'il n'existe pas de tels 
#Le but est de trouver la valeur de i et de j à l'aide d'un discriminant et de vérifier si c'est
#des entiers
def diff_et_som(n,m):
    
    discr_1=1-4*3*2*(-P(n)-P(m))
    if discr_1<0:
        return False
    i=1/6+((discr_1)**(1/2))/6
    if int(i)!=i:
        return False,0,0
    
    discr_2=1-4*3*2*(-P(n)+P(m))
    if discr_2<0:
        return False
    j=1/6+((discr_2)**(1/2))/6
    if int(j)!=j:
        return False,0,0
    return True,int(i),int(j)


#On recherche les pentagonaux de somme et différence pentagonal de
#distance minimale
def recherche_min(max_D,max_i):
    m=-1
    for D in range(1,max_D):
        for j in range(1,max_i-D):
            a,b,c=diff_et_som(j+D,j)
            if a and b!=c:
                if m<0:
                    m=b-c
                
                if b-c<m:
                    m=b-c
                    
    return m
    
#Recherche deux indices i,j tels que i>j et Pi Pj respectent les
#conditions
def recherche(maxi):
    for m in range(1,maxi):
        for n in range(m+1,maxi):
            a,b,c=diff_et_som(n,m)
            if a:
                return n,m
                
#Donne la bonne réponse pour 10000 même si cet algorithme ne prouve pas
#la minimalité