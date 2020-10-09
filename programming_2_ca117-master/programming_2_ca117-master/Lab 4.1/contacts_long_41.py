import sys
contacts = {}
mail = {}

def sorting(word):
	for i in word:
		words = i.split()
		contacts[words[0]] = words[1]
		mail[words[0]] = words[2]
	outcome(sys.stdin.readlines())

def outcome(name):
	for i in name:
		details = i.rstrip('\n')
		if details in contacts:
			print('Phone:', contacts[details])
			print('Email:', mail[details])
		else:
			print('No such contact')

def main():
	with open(sys.argv[1], 'r') as f:
		(sorting(f.readlines()))

	

if __name__ == '__main__':
	main()
