class Score(object):
	def __init__(self, goal=0, score=0):
		self.goal = goal
		self.score = score

	def __str__(self):
		return '{} goal(s) and {} point(s)'.format(self.goal, self.score)
	
	def __mul__(self, other):
		try:
			return Score((self.goal * other), (self.score * other))
		except:
			return Score((self * other.goal), (self * other.score))

	def __gt__(self, other):
		return ((self.goal * 3 + self.score) > (other.goal * 3 + other.score))

	def __rmul__(self, other):
		return Score(self.goal * other, self.score * other)

	def __imul__(self, other):
		self.goal *= other
		self.score *= other
		return self


def main():

    # Create some instances of Score
    s1 = Score()
    s2 = Score(3, 12)
    s3 = Score(4, 9)
    s4 = Score(2, 11)
    s5 = Score(1, 1)

    # Display
    print('Display...')
    print(s1)
    print(s2)
    print(s3)
    print(s4)

    # Multiplication
    print('Multiplication...')
    s2 = s2 * 2
    print(s2)
    print(s2 > s3)

    # Right multiplication
    print('Right multiplication...')
    s2 = 2 * s2
    print(s2)
    print(s2 > s3)

    # In-place multiplication
    print('In-place multiplication...')
    s2alias = s2
    s2 *= 2
    print(s2)
    print(s2alias)
    print(s2 == s2alias)

if __name__ == '__main__':
    main()
