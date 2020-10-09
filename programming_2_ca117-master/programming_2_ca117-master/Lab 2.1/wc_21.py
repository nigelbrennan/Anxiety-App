import sys

lines = sys.stdin.readlines()
leng = 0

i = 0
while i < len(lines):
   	line = lines[i]
   	details = line.split()
   	leng = leng + len(details)
   	i = i + 1

print (leng)
