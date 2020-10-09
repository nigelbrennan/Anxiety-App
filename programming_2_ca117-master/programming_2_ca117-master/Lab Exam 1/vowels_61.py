import sys

def vowels(word):
	vov = ['a', 'e', 'i', 'o', 'u']
	char = []
	for i in word:
		i = i.rstrip('\n')
		char.append(i)
	
	for i in char:
		other = []
		for l in i:
			if l.lower() in vov:
				other.append(l.lower())
		if other == vov:
			print(i)

def main():
	vowels(sys.stdin.readlines())

if __name__ == '__main__':
	main()
