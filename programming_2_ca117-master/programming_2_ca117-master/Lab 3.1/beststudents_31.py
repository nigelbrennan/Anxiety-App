import sys

def student(word):
	high = 0
	name = ''
	text = word.rstrip('\n')
	text = text.split('\n')
	for i in text:
		details = i.split()
		if details[0].isdigit():
			if int(details[0]) >= high:
				if int(details[0]) > high:
					name = ' '.join(details[1:3])
				elif int(details[0]) == high:
					name = name + ', ' + ' '.join(details[1:3])
				high = int(details[0])

		else:
			print('Invalid mark', str(details[0]), 'encountered. Skipping.')
	return 'Best student(s):', name + '\n' + 'Best mark:', high

def main():
	with open(sys.argv[1], 'r') as f:
		print(*student(f.read()))

if __name__ == '__main__':
	main()
