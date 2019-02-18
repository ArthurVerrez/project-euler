#PE15
#15/07/2016
#137846528820

def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

#En raisonnant avec des permutations de 20*[1]+20*[0]
#La réponse est int(fact(40)/(fact(20)*fact(20)))
