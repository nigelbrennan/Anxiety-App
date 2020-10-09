import sys
import string


def remove(text):
	frequency = {}
	output = []
	details = text.split()
	punc = set(string.punctuation)

	if "'" in punc:
		punc.remove("'")

	for i in range(len(details)):
		new_detail = ""
		for l in details[i]:
			if not l in punc:
				new_detail += l
		details[i] = new_detail

	for i in range(len(details)):
		details[i] = details[i].lower()
	
	for i in details:
		if not i in frequency:
			frequency[i] = 1
		else:
			frequency[i] += 1

	for i in frequency:
		output.append(i+' '+':'+' '+str(frequency[i]))
	output = sorted(output)

	for i in output:
		print (i)


def main():
	remove(sys.stdin.read())

if __name__ == '__main__':
	main()
