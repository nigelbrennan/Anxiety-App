import sys

a = 0
aeiou = []
al = []
amik = []
ee = []

def comps(word):
	word = word.split()
	print('Words containing 17 letters:', [x for x in word if len(x) == 17])
	print('Words containing 18+ letters:', [x for x in word if len(x) > 17])
	[aeiou.append(x) for x in word if 'a' in x.lower() and 'e' in x.lower() and 'i' in x.lower() and 'o' in x.lower() and 'u' in x.lower()]
	short()
	[abc(x) for x in word if 'a' in x.lower()]
	print("Words with 4 a's:", amik)
	[qqq(x) for x in word if 'q' in x.lower()]
	print("Words with 2+ q's:", al)
	print('Words containing cie:', [x for x in word if 'cie' in x.lower()])
	print('Anagrams of angle:', [x for x in word if len(x) == 5 and x.lower() != 'angle' and 'a' in x.lower() and 'n' in x.lower() and 'g' in x.lower() and 'e' in x.lower() and 'l' in x.lower()])
	[iary(1) for x in word if x.endswith('iary')]
	print('Words ending in iary:', a)
	print('Words with q but no u:', [x for x in word if ('q' in x or 'Q' in x) and not ('u' in x or  'U' in x)])
	[ee.append(x) for x in word if 'e' in x]
	eee()
	
	
def iary(x):
	global a 
	a = a + x

def short():
	global aeiou
	a = 0
	pos = 0
	i = 0
	while i < len(aeiou):
		if i == 0:
			a = len(aeiou[i])
			pos = i
		
		if len(aeiou[i]) < a:
			a = len(aeiou[i])
			pos = i
		i += 1
	print('Shortest word containing all vowels:', aeiou[pos])		



def abc(x):
	d = 0
	for i in x:
		if i.lower() == 'a':
			d += 1
	if d == 4:
		amik.append(x)

def qqq(x):
	global al
	d = 0
	for i in x:
		if i.lower() == 'q':
			d += 1
	if d > 1:
		al.append(x)

def eee():
	global ee
	eeee = []
	e = 0
	i = 0
	while i < len(ee):
		e1 = 0
		for m in ee[i].lower():
			if m == 'e':
				e1 += 1
		if e < e1:
			e = e1
		i += 1
	
	for w in ee:
		e1 = 0
		for m in w.lower():
			if m == 'e':
				e1 += 1
		if e == e1:
			eeee.append(w)
	print("Words with most e's:", eeee)


def main():
	comps(sys.stdin.read())


if __name__ == '__main__':
	main()


