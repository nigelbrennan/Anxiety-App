import sys

def vowels(word):
	names = []
	for i in word:
		i = i.rstrip('\n')
		names.append(i)
	awg = 0
	for i in names:
		awg += len(i)

	print('Average: {:.2f}'.format(float(awg / len(names))))

	awg = awg // len(names)
	opt = []
	for i in names: 
		if len(i) > awg:
			opt.append(i)
	print(opt)


def main():
	vowels(sys.stdin.readlines())

if __name__ == '__main__':
	main()
