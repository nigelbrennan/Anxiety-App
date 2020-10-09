import sys
from math import sqrt

def func(n):
    for i in n:
        i = i.rstrip('\n')
        i = i.split()
        roots(i[0], i[1], i[2])

def roots(a, b, c):
    r1 = 0
    r2 = 0
    try:
        r1 = (- int(b) + sqrt((int(b) ** 2) - (4 * int(a) * int(c)))) / (2 * int(a))
        r2 = (-int(b) - sqrt((int(b) ** 2) - (4 * int(a) * int(c)))) / (2 * int(a))
        print('r1 = {}, r2 = {}'.format(r1, r2))
    except:
        print ('None')
    

def main():
    func(sys.stdin.readlines())
    
if __name__ == '__main__':
    main()