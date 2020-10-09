import sys

def swap(st):
	for i in st:
		i = i.rstrip('\n')
		i = i.split()
		i[2] = i[2][2:4]
		if i[1] == 'January':
			i[1] = '1'
		elif i[1] == 'February':
			i[1] = '2'
		elif i[1] == 'March':
			i[1] = '3'
		elif i[1] == 'April':
			i[1] = '4'
		elif i[1] == 'May':
			i[1] = '5'
		elif i[1] == 'June':
			i[1] = '6'
		elif i[1] == 'July':
			i[1] = '7'
		elif i[1] == 'August':
			i[1] = '8'
		elif i[1] == 'September':
			i[1] = '9'
		elif i[1] == 'October':
			i[1] = '10'
		elif i[1] == 'November':
			i[1] = '11'
		else:
			i[1] = '12'
		print('/'.join(i))
						
	
def main():
	swap(sys.stdin.readlines())

if __name__ == '__main__':
	main()
