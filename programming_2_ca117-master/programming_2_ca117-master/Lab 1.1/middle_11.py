import sys
n = sys.argv[1]
c = int(len(n) / 2)

if len(n) % 2 != 0:
	print (n[c])
else:
	print ('No middle character!')

