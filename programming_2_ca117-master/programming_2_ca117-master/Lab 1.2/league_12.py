import sys

h1 = 'POS'
h2 = 'CLUB'
h3 = 'P'
h4 = 'W'
h5 = 'D'
h6 = 'L'
h7 = 'GF'
h8 = 'GA'
h9 = 'GD'
h10 = 'PTS'

print('{:>3s} {:20s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(h1, h2, h3, h4, h5, h6, h7, h8, h9, h10))

for line in sys.stdin:
	details = line.split()
	i = 1
	while i < len(details):
		if details[i].isdigit():
			print('{:>3s} {:20s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(details[0], ' '.join(details[1:i]), details[i], details[i + 1], details[i + 2], details[i + 3], details[i + 4], details[i + 5], details[i + 6], details[i + 7]))
			break
		i = i + 1
