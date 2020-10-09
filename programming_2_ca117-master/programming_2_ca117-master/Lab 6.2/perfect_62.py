import sys

def sumFac(n):
    for i in n:
        i = i.rstrip('\n')
        #print(i)
        total = 0
        i2 = 1
        while i2 < int(i):
            if int(i) % i2 == 0:
                total += i2
            i2 += 1
        if int(i) == total:
            print('True')
        else:
            print('False')
    
def main():
    sumFac(sys.stdin.readlines())
    
    
if __name__ == '__main__':
    main()