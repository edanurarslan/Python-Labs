int1=int(input())

total=0

for j in int1:
	total+=int(j)

	if j%total==0:
		print("true")
	else:
		print("false")
