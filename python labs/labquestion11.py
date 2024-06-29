def game(n):
	snake=1
	food=0
	length=n**2
	
	while True:
		if (snake*2)<=length:
			snake*=2
			food+=1
		else:
			return food

n=int(input())
print(game(n))
