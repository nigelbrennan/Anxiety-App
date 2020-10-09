import sys

n = int(sys.argv[1])  #number of stars in the longest line
i = 1		      #line number
s = '*'		      #star ....
sp = ' '	      #space ....
nss = n - 1	      #no. of spaces at the start

while i < n:
	print ((sp * nss) + ((s + sp) * (i - 1)) + s + sp)
	i = i + 1
	nss = nss - 1

while i >= 1:
	if i == n:
		print ((s + sp) * (i - 1) + s + sp)
	else:	
		print ((sp * nss) + ((s + sp) * (i - 1)) + s + sp)
	i = i - 1 
	nss = nss + 1

