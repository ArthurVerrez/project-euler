#PE22
#15/07/2016
#871198282

def quicksort(t):
    if t==[]:
        return []
    up=[]
    down=[]
    for i in t[:len(t)-1]:
        if i>t[-1]:
            up.append(i)
        else:
            down.append(i)
    return quicksort(down)+[t[-1]]+quicksort(up)

def name_alph_val(n):
    v=0
    for i in n:
        v+=ord(i)-64
    return v

def name_scores():
    file=open("PE22_names.txt")
    s=file.read()
    file.close()

    aux=""
    names=[]
    for i in s:
        if i==" ":
            names.append(aux)
            aux=""
        else:
            aux += i

    names=quicksort(names)
    total=0
    for i in range(len(names)):
        total += name_alph_val(names[i])*(i+1)
    return total
    
    
    
