str1=input()
str2=input()

chars1=[]
chars2=[]

number1=[]
number2=[]


for i in str1:
	chars1+=i
for i in str2:
	chars2+=i

for i in range(0, 10):
	int1=int(input())
	number1.append(int1)
for i in range(0, 10):
	int2=int(input())
	number2.append(int2)

def game(str1, str2, number1, number2):

	ex1=[]
	ex2=[]

	delete1=[]
	delete2=[]


	for j in number1:
		if j<=23:
			ex1.append(i+2)
		elif j==24:
			ex1.append(0)
		elif j==25:
			ex1.append(i)
	for j in number2:
		if j<=23:
			ex2.append(i+2)
		elif j==24:
			ex2.append(0)
		elif j==25:
			ex2.append(i)
	
	for j in ex2:
		delete1.append(chars1)
	for j in ex1:
		delete2.append(chars2)

	for i in delete1:
		chars1.remove(i)
	for i in delete2:
		chars2.remove(i)

	total1=0
	total2=0
	
	for i in range(0.10):
		if ord(chars1[i])>ord(chars2[i]):
			total1+=ord(chars1[i])-ord(chars2[i])
		elif ord(chars1[i])<ord(chars2[i]):
			total2+=ord(chars2[i])-ord(chars1[i])

	liste=[total1, total2]
	return liste

	
print (game(str1, str2, number1, number2))



