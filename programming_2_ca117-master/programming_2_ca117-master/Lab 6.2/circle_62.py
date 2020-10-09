from math import sqrt

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    distance = 0
    total_radius = r1 + r2
    x = x1 - x2
    y = y1 - y2
    
    if x < 0:
        x = x * -1
    if y < 0:
        y = y * -1
        
    distance = sqrt((x ** 2) + (y ** 2))
    
    if distance < total_radius:
        return 'True'
    else:
        return 'False'
    
def main():
    print(overlap())
    print(overlap(10))
    print(overlap(10,10))
    print(overlap(10,10,10))
    print(overlap(10,0,10))
    print(overlap(10,0,1,8,0,1))
    print(overlap(10,0,1,8,0,2))

if __name__ == '__main__':
    main()