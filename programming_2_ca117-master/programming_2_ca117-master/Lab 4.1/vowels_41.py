import sys
import string


def remove(text):
	aeiou = {'a':0,
		'e':0,
		'i':0,
		'o':0,
		'u':0,
		}
	punc = set(string.punctuation)
	texts = text.replace(' ', '')
	texts = texts.lower()
	for i in texts:
		if i in aeiou:
			aeiou[i] += 1
	val = sorted(aeiou.values())
	val = val[::-1]
	
	for i in val:
		for l in aeiou:
			if aeiou[l] == i:
				print('{} : {:>3d}'.format(l, i)) 

def main():
	remove(sys.stdin.read())

if __name__ == '__main__':
	main()
