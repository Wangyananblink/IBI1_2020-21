a=1
b=1
print(a)
print(b)
#The first two numbers are 1 and 1, and we output them first.
n=2
for n in range(2,13):
	c=a+b#We use c to store number
	print(c)
	a=b
	b=c
	n=n+1