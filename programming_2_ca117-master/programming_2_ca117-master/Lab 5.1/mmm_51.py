import sys
from statistics import mode

def swap(st):
	num = []
	for i in st:	
		i = i.rstrip('\n')					
		num.append(int(i))
	
	mean = 0.0
	for i in num:
		mean += i

	print('Mean: {:.1f}'.format((mean / len(num))))

	print('Mode: {}'.format((float(mode(num)))))


	num = sorted(num)
	if len(num) % 2 != 0:
		print('Median: {:.1f}'.format(float(num[int((len(num) - 1) / 2)])))
	else:
		print('Median: {:.1f}'.format((float((num[int(len(num) / 2)] + num[(int(len(num) / 2)) - 1]) / 2))))
		
	
def main():
	swap(sys.stdin.readlines())

if __name__ == '__main__':
	main()
