import sys

n = sys.argv[1]

word = sys.stdin.readlines()
tile_values = { 'a':1,'f':4,'k':5,'p':3,'u':1,'z':10,'b':3,'c':3,'d':2, 'e':1,'g':2,'h':4,'i':1,'j':8,'l':1,'m':3,'n':1,'o':1,'q':10,'r':1,'s':1,'t':1,'v':4,'w':4, 'x':8,'y':4,}
words = []
for i in word:
	i = i.rstrip('\n')
	words.append(i)

maxc = 0
pos = 0
i = 0
while i < len(words):
	total = 0
	char = []
	nn = n
	i2 = 0
	while i2 < len(words[i]):
		if words[i][i2] in nn:
			char.append(words[i][i2])
			nn = nn.replace(words[i][i2], '', 1)
		i2 += 1

	for k in char:
		total += tile_values[k]
	
	if total > maxc:
		maxc = total
		pos = i
	i += 1

print (words[pos] + ':', maxc)
