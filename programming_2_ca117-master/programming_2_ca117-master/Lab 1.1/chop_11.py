import sys
n = sys.argv[1]

i = len(n)
while len(n) <= 2:
	break
else:
	print (n[1:len(n) - 1])
