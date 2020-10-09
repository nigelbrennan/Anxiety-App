import sys
n = sys.argv[1]
l = sys.argv[2]
i = 0
p = 0

while i < len(n):
	if n[i] in l:
		p = p + 1
		l = l.replace(n[i], '', 1)
	else:
		p = p
	i = i + 1

if p == len(n):
	print ('True')
else:
	print ('False')
