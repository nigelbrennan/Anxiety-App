from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def distance(self, point):
        d = self.x - point.x
        e = self.y - point.y
        if d < 0:
            d = d * -1
        if e < 0:
            e = e * -1
        return sqrt((e ** 2) + (d ** 2))

    def reflect(self):
        self.x = 0 - self.x
        self.y = 0 - self.y


def main():
    p1 = Point()
    p2 = Point(3,0)
    print('{:.1f}'.format(p1.distance(p2)))
    print('{:.1f}'.format(p2.distance(p1)))
    p3 = Point(3,0)
    p3.reflect()
    print('{:.1f}'.format(p3.distance(p2)))
    p4 = Point(1,1)
    print('{:.1f}'.format(p4.distance(p1)))

if __name__ == '__main__':
    main()
