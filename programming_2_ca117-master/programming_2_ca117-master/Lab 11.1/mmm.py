a = 'abcdefgy012345'
c = 'defgy012345abc'

n = 'gd2 3a'
o = ''

for i in n:
	d = 0
	for val, k in enumerate(c):
		if k == c:
			d = val
			break
	o += a[d]

print(n)
