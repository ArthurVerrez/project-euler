#PE11
#14/07/2016
#70600674


import numpy as np

temp="08022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128642367102638406759547066183864706726206802621220956394396308409166499421245558056673992697177878968314883489637221362309750076442045351400613397343133957817532822753167159403800462161409535692163905429635314755588824001754243629855786560048357189070544443744602158515417581980816805944769287392138652177704895540045208839735991607975732162626793327986688366887576220720346336746551232639353690442167338253911249472180846293240627636206936417230238834629969826759857404361620733529783190017431497148868116235705540170547183515469169233486143520189196748"
grid= np.zeros((20,20),int)
for i in range(20):
    for j in range(20):
        grid[i,j]=int(temp[:2])
        temp=temp[2:]

def down_prod(i,j,n):
    down=1
    for a in range(n):
        down*=grid[i+a,j]
    return down

def right_prod(i,j,n):
    right=1
    for a in range(n):
        right*=grid[i,j+a]
    return right

def diag_r_prod(i,j,n):
    diag=1
    for a in range(n):
        diag*=grid[i+a,j+a]
    return diag

def diag_l_prod(i,j,n):
    diag=1
    for a in range(n):
        diag*=grid[i+a,j-a]
    return diag


def gr_prod(n):
    maxi=0
    for i in range(20):
        for j in range(20):
            if i+n < 20:
                down=down_prod(i,j,n)
                if down > maxi:
                    maxi = down
                if j+n < 20:
                    diag_r=diag_r_prod(i,j,n)
                    if diag_r > maxi:
                        maxi=diag_r
                if j-n >= 0:
                    diag_l=diag_l_prod(i,j,n)
                    if diag_l > maxi:
                        maxi=diag_l
                    
            if j+n < 20:
                right=right_prod(i,j,n)
                if right > maxi:
                    maxi = right
                    
    return maxi
            
