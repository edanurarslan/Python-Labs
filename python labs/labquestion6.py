class Vector():
	def __init__(self, v1, v2, v3, v4, v5, v6):
		self.v1=v1
		self.v2=v2
		self.v3=v3
		self.v4=v4
		self.v5=v5
		self.v6=v6

	def vectors1(self):
		return self.v1, self.v2, self.v3 
	
	def vectors2(self):
		return self.v4, self.v5, self.v6
	
	def mySum(self):
		x1=int(self.v1)+int(self.v4)
		x2=int(self.v2)+int(self.v5)
		x3=int(self.v3)+int(self.v6)
		return x1, x2, x3

	def mySubstraction(self):
		x4=int(self.v1)-int(self.v4)
		x5=int(self.v2)-int(self.v5)
		x6=int(self.v3)-int(self.v6)
		return x4, x5, x6

	def myMultiplication(self):
		x7=int(self.v1)*int(self.v4)+int(self.v2)*int(self.v5)+int(self.v3)*int(self.v6)
		return x7

	
	
v1=input()
v2=input()
v3=input()
v4=input()
v5=input()
v6=input()

mylist=[]
mylist.append(v1)
mylist.append(v2)
mylist.append(v3)
mylist.append(v4)
mylist.append(v5)
mylist.append(v6)

myvector=Vector(mylist[0], mylist[1], mylist[2], mylist[3], mylist[4], mylist[5])

print(myvector.vectors1())
print(myvector.vectors2())
print(myvector.mySum())
print(myvector.mySubstraction())
print(myvector.myMultiplication())





		
	
	
		
