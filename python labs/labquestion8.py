a=int(input())
b=int(input())
n=int(input())
total=0

def f(x):
	return (x**4)-(4*x)

def integral(a,b,n):
	delta=(b-a)/n
	return delta

for j in range(a,b+1):
	j=f(j)*integral(j,b,n)
	total+=integral(j,b,n)*f(j)
	

print("{:.4f}".format(total))
	
	


	
	


