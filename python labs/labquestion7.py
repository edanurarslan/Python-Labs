yaricap=int(input())
aci=int(input())


class Kure():
	def __init__(self, yaricap, aci):
		self.yaricap=yaricap
		self.aci=aci
	
	def alan_hacim_hesapla(self):
		alan1=4*3*(yaricap**2)
		hacim1=(4*3*(yaricap**3))/3
		alan1=round(alan1, 2)
		hacim1=round(hacim1, 2)
		return alan1, hacim1

class KureDilimi():
		
	def __init__(self, yaricap, aci):
		self.yaricap=yaricap
		self.aci=aci
		
	def kure_dilimi_alan_hacim_hesapla(self):
		alan2=(4*3*(yaricap**2)*aci)/360
		hacim2=(4*3*(yaricap**3)*aci)/1080
		alan2=round(alan2, 2)
		hacim2=round(hacim2, 2)
		return alan2, hacim2

mylist=[]
mylist.append(yaricap)
mylist.append(aci)

mykure=Kure(mylist[0], mylist[1])

mylist2=[]
mylist2.append(yaricap)
mylist2.append(aci)

mykure2=KureDilimi(mylist2[0], mylist2[1])

print(mykure.alan_hacim_hesapla())
print(mykure2.kure_dilimi_alan_hacim_hesapla())
		
		
