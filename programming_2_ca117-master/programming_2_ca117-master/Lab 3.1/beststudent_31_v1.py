import sys

def student(word):
	high = 0
	name = ''
	text = word.rstrip('\n')
	text = text.split('\n')
	for i in text:
		details = i.split()
		if int(details[0]) > high:
			high = int(details[0])
			name = ' '.join(details[1:3])
	print('Best student:', name)
	print('Best mark:', high)
		
def main():
	with open(sys.argv[1], 'r') as f:
		student(f.read())

if __name__ == "__main__":
	main()
