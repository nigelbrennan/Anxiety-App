def maximum(m, minim = None):
	if not m:
		return minim
	candidate = m.pop()
	if minim == None or candidate > minim:
		return maximum(m, candidate)
	return maximum(m, minim)

def main():
	min = None
	print(maximum([6,5,1,3,4]))
	print(maximum([6,5,11,3,4]))
	print(maximum([6,15,11,13,14]))
	print(maximum([6,15,11,13,4]))

if __name__ == '__main__':
	main()
