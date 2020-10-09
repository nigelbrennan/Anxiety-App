def minimum(m, minim = None):
	if not m:
		return minim
	candidate = m.pop()
	if minim == None or candidate < minim:
		return minimum(m, candidate)
	return minimum(m, minim)

def main():
	min = None
	print(minimum([6,5,1,3,4]))
	print(minimum([6,5,11,3,4]))
	print(minimum([6,15,11,13,14]))
	print(minimum([6,15,11,13,4]))

if __name__ == '__main__':
	main()
