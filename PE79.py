#PE79
#22/04/2017
#73162890

key_file=open("C:/Users/Arthur/Google Drive/Projets/Project Euler/PE79_keylog.txt","r")

keys=key_file.readlines()
for i in range(len(keys)):
    keys[i]=keys[i][:3]

#Remarquons tout d'abord qu'il n'y a jamais deux fois les mêmes chiffres
#dans la même clé, on peut donc en déduire qu'un code minimal ne
#contient pas deux fois le même chiffre
#On peut donc faire une 10-liste représentant les chiffres de 0 à 10
#et l'analyse de chaque clé donne sa place minimal dans le mot de passe

place=10*[-1]
def update_place(key):
    for i in range(len(key)):
        n=int(key[i])
        if i>place[n]:
            place[n]=i
        if i!=0 and place[int(key[i-1])]>=place[n]:
            place[n]=place[int(key[i-1])]+1

#Renvoie l'indice de la première occurence de x dans l
def cherche(l,x):
    for i in range(len(l)):
        if l[i]==x:
            return i

#Trouve le code en considérant que la place est unique
def trouve_code():
    for key in keys:
        update_place(key)
    code=[]
    for i in range(max(place)+1):
        code.append(cherche(place,i))
    return code