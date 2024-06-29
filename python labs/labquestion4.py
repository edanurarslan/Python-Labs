d = {"2":"II", "3":"III", "6":"VI", "7":"VII", "8":"VIII", "1000":"M", "900":"CM", "500":"D", "400":"CD", "100":"C", "90":"XC", "50":"L", "40":"XL", "10":"X", "9":"IX", "5":"V", "4":"IV", "1":"I", "16":"XVI", "26":"XXVI", "99":"XCIX"}

int1=input()

def roma(int1):
	
	if int1 in d.keys():
		print(d.get(int1), end="")

		

roma(int1)
