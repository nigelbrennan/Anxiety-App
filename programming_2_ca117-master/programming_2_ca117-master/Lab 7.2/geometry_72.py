class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def distance(self, point):
		x = self.x - point.x
		if x < 0:
			x = x * -1
		y = self.y - point.y
		if y < 0:
			y = y * -1
		return x / 2, y / 2


	def __str__(self):
		return '({}, {})'.format(self.x, self.y)



class Segment(object):

	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def midpoint(self):
		return Point.distance(self.p1, self.p2)

	def length(self):
		x = self.x - point.x
		if x < 0:
			x = x * -1
		y = self.y - point.y
		if y < 0:
			y = y * -1
		total = ((x ** 2) + (y ** 2)) ** 0.5
		return total

class Circle(object):

	def __init__(self, center, radius):
		self.center = center
		self.radius = radius

	def overlaps(self, c2):
		total_radius = self.radius + c2.radius
		x = self.center.x - c2.center.x
		y = self.center.y - c2.center.y
    
		if x < 0:
			x = x * -1
		if y < 0:
			y = y * -1
        
		distance = ((x ** 2) + (y ** 2)) ** 0.5
    
		if distance < total_radius:
			return 'True'
		else:
			return 'False'
    
def main():
	p1 = Point()
	p2 = Point(5, 5)
	s1 = Segment(p1, p2)
	s2 = Segment(p2, p1)
	c1 = Circle(p1, 5)
	c2 = Circle(p2, 2)
	c3 = Circle(p1, 2)

	print(p1)
	print(p2)

	print(s1.midpoint())
	print(s2.midpoint())
	print(c1.overlaps(c2))
	print(c2.overlaps(c1))
	print(c1.overlaps(c3))
	print(c3.overlaps(c2))

if __name__ == '__main__':
	main()
