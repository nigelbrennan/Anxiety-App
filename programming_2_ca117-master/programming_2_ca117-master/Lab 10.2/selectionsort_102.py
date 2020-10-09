import random

def selectionsort(a):
	i = 0
	while i < len(a):
		p = i              # find p, the
		j = i + 1          # position of the
		while j < len(a):  # smallest element
			if a[j] < a[p]: # in a[i,N)
				p = j        #
			j = j + 1       #

		tmp = a[p]         # swap a[i] and a[p]
		a[p] = a[i]        #
		a[i] = tmp         #

		i = i + 1

def main():
	A = random.sample(range(-99, 100), 10)

	print('Unsorted: {}'.format(A))
	selectionsort(A)
	print('Sorted: {}'.format(A))

if __name__ == '__main__':
	main()
