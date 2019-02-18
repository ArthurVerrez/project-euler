#PE42
#15/07/2016
#162

def name_alph_val(n):
    v=0
    for i in n:
        v+=ord(i)-64
    return v

def tr_word(word):
    val=name_alph_val(word)
    val*=2
    for i in range(1,int(val**(1/2))+1):
        if i*(i+1)==val:
            return True
    return False

def triangle_numbers():
    file=open("PE42_words.txt")
    s=file.read()
    file.close()

    aux=""
    words=[]
    for i in s:
        if i==" ":
            words.append(aux)
            aux=""
        else:
            aux += i

    triangle=0
    for word in words:
        if tr_word(word):
            triangle+=1
    return triangle
    
