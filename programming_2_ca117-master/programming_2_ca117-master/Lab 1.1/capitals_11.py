import sys
n = sys.argv[1]

while len(n) <= 1:
	break

if len(n) >= 2:
	print (n[0].upper() + n[1: len(n) - 1] + n[len(n) - 1].upper())
