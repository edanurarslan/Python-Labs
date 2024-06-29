
def grades():
	xx=True
	grades1=open("mystudents.txt", "w")
	
	while xx==True:
		student=input()
		if student=="X":
			xx==False
			break
		mygrades1=grades1.write(student + "\n")
		
	grades2=open("mystudents.txt", "r")
	mygrades2=grades2.readlines()
	gradelist=[]
	for i in mygrades2:
		name, grade=i.split(" ")
		gradelist.append(int(grade))
	
	total=0
	average=0
	
	for i in gradelist:
		total+=int(i)
		average=total/len(gradelist)
	return average
	
	#for i in gradelist:
		
		
		
	
print(grades())
