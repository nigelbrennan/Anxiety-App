import sys

n = sys.argv[1]           #number
i = int(sys.argv[2])	  #
total = 0
c = 1			  #index

for l in n:
	total = total + (int(l) * i ** (len(n) - c)) 
	c = c + 1

print (total)
