#PE112
#04/05/2017
#1587000

#Essayons tout d'abord une version naïve où on détermine tout simplement si un nombre est bouncy, on les compte et tant qu'on est en dessous de 99% on continue

def bouncy(n):
    s=str(n)
    same=True
    asc=True
    for i in range(1,len(s)):
        if int(s[i])>int(s[i-1]):
            if (not same) and not asc:
                return True
            elif same:
                same=False
        elif int(s[i])<int(s[i-1]):
            if (not same) and asc:
                return True
            elif same:
                same=False
                asc=False
    return False

def ans_under(p):
    r=0
    i=1
    while r/i <p:
        i+=1
        r+=int(bouncy(i))
    return i