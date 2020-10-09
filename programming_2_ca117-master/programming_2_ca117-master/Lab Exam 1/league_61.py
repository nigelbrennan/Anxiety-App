import sys

n = sys.stdin.readlines()

words = []
for i in n:
	i = i.rstrip('\n')
	words.append(i)

cc = {}
s = []
for i in words:
	total = 0
	details = i.split(':')
	details[1] = details[1].strip()
	score = details[1].split()
	for k in score:
		if k.isdigit():
			total += int(k)
		else:
			total = 0
			break
	
	if total != 0:
		cc[total] = details[0]
		s.append(total)
s = sorted(s)
m = len(s) - 1
while m >= 0:
	print(cc[s[m]] + ':', s[m], 'points')
	m = m - 1
