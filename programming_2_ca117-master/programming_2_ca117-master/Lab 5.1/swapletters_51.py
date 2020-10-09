import sys

def swap(st):
	opt = ''
	i = 0
	if len(st) % 2 != 0:
		i = len(st) - 1
	else:
		i = len(st)
	i2 = 1
	while i2 < i:
		if i2 % 2 != 0:
			opt = opt + st[i2] + st[i2 - 1]
		i2 += 1

	if len(st) % 2 != 0:
		opt = opt + st[len(st) - 1]

	print(opt) 
			

def main():
	swap(sys.argv[1])

if __name__ == '__main__':
	main()
