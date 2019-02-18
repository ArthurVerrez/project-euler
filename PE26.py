#PE26
#07/07/2016
#[982, 983]

from decimal import *

#renvoie la longueur du cycle d'une chaine de caractère
#ver est le nombre de répétitions à considérer avant de considérer
#une séquence comme un cyle

def cycle(s,ver):
    for d in range(2,(len(s)//ver)):
        for i in range(d,len(s)-d+1,d):
            if not s[0:d]==s[i:i+d]:
                break
            if i-(len(s)-d)<=d:
                return d
    return 0

#start_ver est exclusif
def cycle_s(s,ver,start_ver):
    for start in range(0,start_ver):
        d=cycle(s[start::],ver)
        if d>0:
            return d
    return 0


def rec_cycles(n,ver,start_ver,maxi):
    m=[0,0]
    for d in range(2,n+1):
        getcontext().prec=maxi*ver+1+start_ver
        s=str(Decimal(1)/Decimal(d))[2::]
        if len(s)>=maxi*ver+1+start_ver:
            c=cycle_s(s,ver,start_ver)
            if c>m[0]:
                m=[c,d]
    return m
        
