import sys
import re

ip_address = r'\b(?:(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b'
name = 'Mr*s*(?:\s[A-Z]\w*){0,4}'



def main():

	name_regex = re.compile(name)
	ip_address_regex = re.compile(ip_address)

	s = sys.stdin.read()

	namelist = name_regex.findall(s)
	for n in namelist:
		print(n)

	iplist = ip_address_regex.findall(s)
	for ip in iplist:
		print(ip)

if __name__ == '__main__':
	main()
