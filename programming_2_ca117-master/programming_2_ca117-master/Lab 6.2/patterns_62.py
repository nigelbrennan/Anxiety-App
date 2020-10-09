import sys
import re

def pattern(n):
    date_1 = re.compile('\d{1,2}/\d{1,2}/\d{2,4}')
    date_2 = re.compile('\d{1,2}-\d{1,2}-\d{2,4}')
    date_3 = re.compile('\d{1,2}[/-]\d{1,2}[/-]\d{2,4}')
    email = re.compile('\S{1,50}\@\S{1,50}\w{1,3}')
    phone = re.compile('01[\s-]\d{7,8}')
    date_4 = re.compile('\d{1,2}\s\w{3}\s\d{2,4}')
    print(date_1.findall(n))
    print(date_2.findall(n))
    print(date_3.findall(n))
    print(phone.findall(n))
    print(email.findall(n))
    print(date_4.findall(n))
    
def main():
    pattern(sys.stdin.read())
    
if __name__ == '__main__':
    main()