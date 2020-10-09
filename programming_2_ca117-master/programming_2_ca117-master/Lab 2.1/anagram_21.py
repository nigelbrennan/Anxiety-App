import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
	line = lines[i]
	details = line.split()
	leng = 0
	for o in details[1]:
		if o in details[0]:
			leng += 1
	if leng == len(details[0]):
		print ('True')
	else:
		print('False')

	i = i + 1


