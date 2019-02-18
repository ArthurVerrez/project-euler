#PE31
#03/08/2016
#73682

coins=[1,2,5,10,20,50,100,200]


#Renvoie les combinaisons possibles de faire p cents avec des coins au dessus ou égal au a_ème élement de coins
#s est la somme des élements dans pos
def poss(p,prec,s,a):
    if s+coins[a]>p:
        return []
    r=[]
    aux=[]
    for i in enumerate(coins[a::]):
        if s+i[1] == p:
            r.append(prec+[i[1]])
        if s+i[1] < p:
            aux=poss(p,prec+[i[1]],s+i[1],a+i[0])
            for j in aux:
                r.append(j)
    return r

def possibilities(p):
    return len(poss(p,[],0,0))
    
    
