import sys

def poker(hand):
	nothing = 0
	pair1 = 0
	pair2 = 0
	three = 0
	straight = 0
	flush = 0
	full_house = 0
	four = 0
	straight_flush = 0
	royal = 0
	hand = hand.rstrip('\n')
	hands = hand.split('\n')
	leng =  len(hands)
	for i in hands:
		details = i.split(',')
		if int(details[10]) == 0:
			nothing += 1
		elif int(details[10]) == 1:
			pair1 += 1
		elif int(details[10]) == 2:
			pair2 += 1
		elif int(details[10]) == 3:
			three += 1
		elif int(details[10]) == 4:
			straight += 1
		elif int(details[10]) == 5:
			flush += 1
		elif int(details[10]) == 6:
			full_house += 1
		elif int(details[10]) == 7:
			four += 1
		elif int(details[10]) == 8:
			straight_flush += 1
		elif int(details[10]) == 9:
			royal += 1

	print('The probability of nothing is {:.4f}%'.format(nothing/leng*100))
	print('The probability of one pair is {:.4f}%'.format(pair1/leng*100))
	print('The probability of two pairs is {:.4f}%'.format(pair2/leng*100))
	print('The probability of three of a kind is {:.4f}%'.format(three/leng*100))
	print('The probability of a straight is {:.4f}%'.format(straight/leng*100))
	print('The probability of a flush is {:.4f}%'.format(flush/leng*100))
	print('The probability of a full house is {:.4f}%'.format(full_house/leng*100))
	print('The probability of four of a kind is {:.4f}%'.format(four/leng*100))
	print('The probability of a straight flush is {:.4f}%'.format(straight_flush/leng*100))
	print('The probability of a royal flush is {:.4f}%'.format(royal/leng*100))
	

def main():
	poker(sys.stdin.read())


if __name__ == '__main__':
	main()
