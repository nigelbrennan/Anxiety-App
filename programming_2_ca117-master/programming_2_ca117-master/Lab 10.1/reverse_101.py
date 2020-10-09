def reverse_list(n):
	if not n:
		return []
	return [n[-1]] + reverse_list(n[:-1])

def main():
	print(reverse_list([1,2,3]))
	print(reverse_list([3,4,5,6]))
	print(reverse_list([1,2]))

if __name__ == '__main__':
	main()
