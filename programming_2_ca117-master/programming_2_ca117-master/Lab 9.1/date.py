import sys
import re

name = r'\b(?:(?:0[0-9]|[1-2][0-9]|3[0-1])/){2}(?:0[0-9]|[1-2][0-9]|3[0-1])\b'


def main():

	name_regex = re.compile(name)

	s = sys.stdin.read()

	namelist = name_regex.findall(s)
	for n in namelist:
		print(n)


if __name__ == '__main__':
	main()
