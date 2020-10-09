import sys

def swap(st):
	for i in st:
		i = i.rstrip('\n')
		o = i.lower()
		if 'e' in o and 'v' in o and 'i' in o and 'l' in o:
			evil = []
			for l in o:
				if l == 'e' or l == 'v'	or l == 'i' or l == 'l':
					evil.append(l)
			if len(evil) == 4 and evil[0] == 'e' and evil[1] == 'v' and evil[2] == 'i' and evil[3] == 'l':
				print (i)
						
	
def main():
	swap(sys.stdin.readlines())

if __name__ == '__main__':
	main()
