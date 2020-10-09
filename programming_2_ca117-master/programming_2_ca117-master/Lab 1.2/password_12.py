import sys

n = sys.argv[1]
c = 0
m = 0
v = 0
z = 0

i = 0
while i < len(n):
	if n[i].isupper():
		v = 1
	elif n[i].islower():
		m = 1
	elif n[i].isdigit():
		c = 1
	else:
		z = 1
	i = i + 1

print (c + m + v + z) 
	
