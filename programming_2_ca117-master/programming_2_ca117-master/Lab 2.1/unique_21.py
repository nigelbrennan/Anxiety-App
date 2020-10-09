import sys
import string

lines = sys.stdin.read()
punct = set(string.punctuation)
out = []

for i in lines:
	if i in punct:
		lines = lines.replace(i, '')

lines = lines.lower()
lines = lines.split()

for i in lines:
	if not i in out:
		out.append(i)

print (len(out))
