# What does this piece of code do?
# Answer: After runing a few times, I found that the numbers were always less than 51, when I changed the signal "<" to ">" , they were always bigger than 50.
# Code's function: Selects a random number between 1 and 100 until a number less than 50 is selected, which is then printed

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False
while p==False:
	p = True
	n = randint(1,100)
	if n > 50:
		p = False

print(n)