class Weight(object):
	OUNCES_PER_POUND = 16
	def __init__(self, pound = 0, ounces = 0):
		if ounces > 16:
			self.pound = pound + (ounces // 16)
			self.ounces = ounces % 16
		else:
			self.pound = pound
			self.ounces = ounces

	def __str__(self):
		return '{} pound(s) and {} ounce(s)'.format(self.pound, self.ounces)

	def __eq__(self, other):
		return (self.pound + (self.ounces / 100)) == (other.pound + (other.ounces / 100))

	def __gt__(self, other):
		return (self.pound + (self.ounces / 100)) > (other.pound + (other.ounces / 100))

	def __ge__(self, other):
		return (self.pound + (self.ounces / 100)) >= (other.pound + (other.ounces / 100))

	def __mul__(self, other):
		return Weight(self.pound * other, self.ounces * other)

	def __rmul__(self, other):
		return Weight(self.pound * other, self.ounces * other)

	def __sub__(self, other):
		return Weight((self.pound - other.pound), (self.ounces - other.ounces))

	def __isub__(self, other):
		self.pound -= other.pound
		self.ounces -= other.ounces
		return self

	def __add__(self, other):
		return Weight(self.pound + other.pound, self.ounces + other.ounces)

	def __iadd__(self, other):
		if self.ounces + other.ounces > 16:
			self.pound += other.pound + ((self.ounces + other.ounces) // 16)
			self.ounces = ((self.ounces + other.ounces) % 16)
		else:
			self.pound += other.pound
			self.ounces += other.ounces
		return self

	def __imul__(self, other):
		self.pound *= other
		self.ounces *= other
		return self

	def from_ounces(n):
		m = n // 16
		k = n % 16
		return Weight(m, k)


def main():

	# Create some weights
	d1 = Weight()
	d2 = Weight(3, 12)
	d3 = Weight(8, 6)

	# Display ounces per pound
	print('Ounces in a pound: {}'.format(Weight.OUNCES_PER_POUND))

	# Display weights
	print('Weights...')
	print('d1 : {}'.format(d1))
	print('d2 : {}'.format(d2))
	print('d3 : {}'.format(d3))

	# Equality
	print('Equality...')
	print(Weight(4, 4) == Weight(4, 4))
	print(d2 == d3)
	print(d2 != d3)

	# Greater than, greater than or equal to
	print('Greater than, greater than or equal to...')
	print(d2 > d1)
	print(d1 >= d2)

	# Less than, less than or equal to
	print('Less than, less than or equal to...')
	print(d1 < d2)
	print(d1 <= d1)

	# Addition
	print('Addition...')
	d4 = d2 + d3
	print('d4 : {}'.format(d4))
	print(d4 > d2)

	# In-place addition
	print('In-place addition...')
	d2_alias = d2
	d2 += d3
	print('d2 : {}'.format(d2))
	print(d2 > d3)
	print(d2_alias == d2)

	# Multiplication
	print('Multiplication...')
	d5 = d3 * 2
	print('d5 : {}'.format(d5))

	# In-place multiplication
	print('In-place multiplication...')
	d6 = Weight(1, 1)
	d6_alias = d6
	d6 *= 2
	print('d6 : {}'.format(d6))
	print(d6_alias == d6)
	print(d6 > d1)

	# Right multiplication
	print('Right multiplication...')
	d7 = 3 * d6
	print('d7 : {}'.format(d7))
	print(d6 < d7)

	# Subtraction
	print('Subtraction...')    
	d8 = d7 - d6
	print('d8 : {}'.format(d8))
	print(d8 < d7)

	# In-place subtraction
	print('In-place subtraction...')
	d7_alias = d7
	d7 -= d6
	print('d7 : {}'.format(d7))
	print(d7_alias == d7)
	
	# From ounces
	print('From ounces...')
	d9 = Weight.from_ounces(100)
	print('d9 : {}'.format(d9))
	print(d9 > d7)

if __name__ == '__main__':
	main()

