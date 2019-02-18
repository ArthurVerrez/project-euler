#PE17
#06/07/2016
#21124


#Only works for 0 <= n < 10000 and integer
def number_to_letter(number):
    if number==0:
        return "zero"
    
    base=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    higher=["hundred", "thousand"]
    
    def aux(n):
        
        m=list(str(n))
        lenm=len(m)
        
        if lenm < 2:
            return base[n]
        if lenm == 2:
            if m[0] == '1':
                return base[n]
            else:
                return(tens[int(m[0])] + " " + aux(n%(10**(lenm-1))))
                       
        if lenm  < 5:
            first = higher[lenm - 3]
            if lenm == 3:
                if n%(10**(lenm-1)) == 0:
                    return(base[int(m[0])] + " "+ first)
                
                return(base[int(m[0])] + " "+ first + " " + "and " + aux(n%(10**(lenm-1))))
            else:
                if n%(10**(lenm-1)) == 0:
                    return(base[int(m[0])] + " "+ first)
                
                return(base[int(m[0])] + " "+ first + ", " + aux(n%(10**(lenm-1))))
        
    return aux(number)


def count(mot):
    s=0
    for i in mot:
        if i not in " ,-":
            s+=1
    return s

def count_letters_until(n):
    total = 0
    
    for i in range(1,n+1):
        word=number_to_letter(i)
        total+=count(word)
    return total

