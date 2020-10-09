import sys

n = str(sys.argv[1])
vowels = ['a', 'e', 'i', 'o', 'u',]

if n.endswith('ch') or n.endswith('sh') or n.endswith('x') or n.endswith('s') or n.endswith('z'):
	print (n + 'es')
elif n.endswith('f'):
	print(n[:len(n)-1] + 'ves')
elif n.endswith('fe'):
	print(n[:len(n)-2] + 'ves')
elif n.endswith('o'):
	print(n + 'es')
elif (n[len(n) - 1] == 'y') and (n[len(n) - 2] not in vowels):
	print(n[:len(n)-1] + 'ies')
else:
	print(n + 's')
