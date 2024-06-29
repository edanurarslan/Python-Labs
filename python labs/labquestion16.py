psw=input()

def password(psw):
	x=["@", "#", "*", "?"]
	flag1=""
	flag2=""
	flag3=""
	for j in psw:
		if j in x and flag1=="":
			flag1+="True"

	for j in psw:
		if 65<=ord(j)<=90 and flag2=="":
			flag2+="True"

	for j in psw:
		if 97<=ord(j)<=122 and flag3=="" :
			flag3+="True"
	
	if flag1=="True" and flag2=="True" and flag3=="True":
		return True
	else:
		return False


print(password(psw))

