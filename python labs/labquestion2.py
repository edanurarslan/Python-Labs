data_catalog=input()
data_frequency=input()

import ast
catalog=ast.literal_eval(data_catalog)
frequency=ast.literal_eval(data_frequency)


def piechart(cata, freq):

	total=0
	a=[]
	c=[]
	
	for i in freq:
		total+=i
	
	b=360/total
	
	for j in range(len(freq)):
		a+=[int(b*freq[j])]


	for i in range(len(a)):
		c+=[[cata[i], a[i]]]

	return c

print(piechart(catalog, frequency))

	
			
