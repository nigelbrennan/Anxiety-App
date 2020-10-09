import sys

def name(n):
	t = n.split()
	k = []
	for val, i in enumerate(t):
		if i == "Mr" or i == 'Mrs' or i == 'Ms':
			k.append(i)
			p = 1
			while p > 0:
				if t[val + p][0].isupper() and t[val + p] != 'Mr' and t[val + p] != 'Mrs' and t[val + p] != 'Ms':
					k.append(t[val + p].rstrip('.'))
					p += 1
				else:
					print(' '.join(k))
					k = []
					p = 0
		
	ip_address(n)

def ip_address(n):
	
	ip = re.compile('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')
	ips = ip.findall(n)
	for i in ips:
		i = i.split('.')
		m = 0
		for a in i:
			if int(a) < 256 and int(a) >= 0:
				m += 1
		if m == len(i):
			print ('.'.join(i))

def main():
	name(sys.stdin.read())

if __name__ == '__main__':
	main()
