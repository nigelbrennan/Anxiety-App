import sys

def swap(st):
	runners = []
	for i in st:	
		i = i.rstrip('\n')
		i = i.split()				
		o = 1
		bt = 0
		pos = 0
		while o < len(i):
			time = i[o].split(':')

			if not time[0].isdigit():
				break

			if not time[1].isdigit():
				break

			if o == 1:
				bt = (int(time[0]) * 60) + int(time[1])

			pt = (int(time[0]) * 60) + int(time[1])

			if pt < bt:
				bt = pt
				pos = o

			o += 1

		if o == len(i):
			runners.append(i[0] + ' ' + str(i[pos]))
	
	ot = 0
	op = 0
	k = 0
	while k < len(runners):
		i = runners[k].split()
		time = i[1]
		time = time.split(':')
		if k == 1:
			ot = (int(time[0]) * 60) + int(time[1])

		pt = (int(time[0]) * 60) + int(time[1])

		if pt < ot:
			ot = pt
			op = k

	
		k += 1
	runners = runners[op].split()
	print(runners[0], ':', runners[1])

	
def main():
	swap(sys.stdin.readlines())

if __name__ == '__main__':
	main()
