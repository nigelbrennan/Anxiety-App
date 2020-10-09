class Customer(object):

	def __init__(self, name, balance, address, city, co):
		self.name = name
		self.balance = balance
		self.address = address
		self.city = city
		self.co = co

	def __str__(self):
		return '{}\n{}\n{}\n{}\nBalance: {:.2f}\nDiscount: 0%\nAmount due: {:.2f}'.format(self.name,self.address, self.city, self.co, self.balance, self.balance)

class ValuedCustomer(Customer):

	def __str__(self):
		return '{}\n{}\n{}\n{}\nBalance: {:.2f}\nDiscount: 10%\nAmount due: {:.2f}'.format(self.name,self.address, self.city, self.co, self.balance,100 - (self.balance * 10) / 100)
def main():

    c1 = Customer('Jimmy', 100, '22 Main Street', 'Naas', 'Kildare');
    c2 = ValuedCustomer('Lucy', 100, '23 Main Street', 'Roosky', 'Roscommon');
    c3 = Customer('Fred', 200, '24 Main Street', 'Sneem', 'Kerry');

    print(c1)
    print(c2)
    print(c3)

if __name__ == '__main__':
    main()
