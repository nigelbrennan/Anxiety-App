import sys

class Contact(object):
	
	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email

	def __str__(self):
		return "{} {} {}\n".format(self.name, self.phone, self.email)

class ContactList(object):

	def __init__(self, d={}):
		self.d = d

	def add_contact(self, n):
		self.d[n.name] = [n.phone, n.email]

	def del_contact(self, n):
		self.d[n] = 0
		del self.d[n]

	def get_contact(self, n):
		if n in self.d:
			return '{} {} {}'.format(n, self.d[n][0], self.d[n][1])
		else:
			return '{} : No such contact'.format(n)

	def __str__(self):
		c_list = 'Contact list\n' + '------------\n'
		for key, value in sorted(self.d.items()):
			c_list += str(Contact(key, value[0], value[1]))
		return c_list.rstrip('\n')


def main():
	cl = ContactList()
	for line in sys.stdin:
		[name, phone, email] = line.strip().split()
		c = Contact(name, phone, email)
		cl.add_contact(c)

	print(cl.get_contact('Jimmy'))
	print(cl.get_contact('Mary'))

	cl.del_contact('Maggie')
	cl.del_contact('Maggie')
	print(cl.get_contact('Mary'))
	print(cl)

	c = Contact('Fred', '085-8776543', 'fred@yahoo.com')
	cl.add_contact(c)
	print(cl)

if __name__ == '__main__':
    main()
