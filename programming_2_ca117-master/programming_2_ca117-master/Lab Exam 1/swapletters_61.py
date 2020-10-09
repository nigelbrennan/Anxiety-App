import sys

def swaping(word):
	opt = ''
	i = 0
	while i < len(word):
		if i % 2 != 0:
			opt += word[i]
			opt += word[i - 1]
		i += 1

	if len(word) % 2 != 0:
		opt += word[len(word) - 1]

	print(opt)

def main():
	swaping(sys.argv[1])

if __name__ == '__main__':
	main()
