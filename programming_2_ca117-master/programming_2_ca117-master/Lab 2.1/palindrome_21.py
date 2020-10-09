import sys

n = str(sys.argv[1:])

n = n.lower()

n = list(n)

i = 0
while i < len(n):
	if n[i].isalpha():
		i = i + 1
	else:
		n.remove(n[i])	


i2 = 0
i3 = len(n) - 1
while i2 < int(len(n)):
	if n[i2] != n[i3]:
		print ('False')
		break
	i2 = i2 + 1
	i3 = i3 - 1
	
if i2 == int(len(n)):
	print('True')
