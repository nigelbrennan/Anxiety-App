import sys
import random

def lotto(numb):
	t = 0
	f = 0
	v = 0
	x = 0
	for i in range(0, 1000000):
		s = 0
		ran = random.sample(range(1, 47), 6)
		for i in ran:
			if str(i) in numb:
				s += 1
		if s == 3:
			t += 1
		elif s == 4:
			f += 1
		elif s == 5:
			v += 1
		elif s == 6:
			x += 1
		s = 0

	z = ''
	if x == 0:
		z = '?'
	else:
		z = str(1000000 / x)

	print("Match 3's : {:>5d} ({} to 1)".format(t, 1000000/t))
	print("Match 4's : {:>5d} ({} to 1)".format(f, 1000000/f))
	print("Match 5's : {:>5d} ({} to 1)".format(v, 1000000/v))
	print("Match 6's : {:>5d} ({} to 1)".format(x, z))

def main():
	lotto(sys.argv[1:])

if __name__ == '__main__':
	main()
