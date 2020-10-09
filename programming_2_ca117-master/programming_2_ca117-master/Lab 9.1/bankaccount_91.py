class BankAccount(object):
	no = 16555231
	def __init__(self, name, surename, balance):
		self.name = name
		self.surename = surename
		self.balance = balance
		BankAccount.no += 1
		self.no = BankAccount.no

class CurrentAccount(BankAccount):
	def __str__(self):
		return 'Name: {} {}\nAccount number: {}\nBalance: {:.2f}\nAccount type: current'.format(self.name, self.surename, self.no, self.balance)
	
	def withdraw(self, n):
		if self.balance - int(n) >= -1000:
			self.balance = self.balance - int(n)
		else:
			print('Insufficient funds available')

	def lodge(self, n):
		self.balance += int(n)

class SavingsAccount(BankAccount):
	def __str__(self):
		return 'Name: {} {}\nAccount number: {}\nBalance: {:.2f}\nAccount type: savings'.format(self.name, self.surename, self.no, self.balance)

	def withdraw(self, n):
		if self.balance - int(n) >= 0:
			self.balance = self.balance - int(n)
		else:
			print('Insufficient funds available')

	def lodge(self, n):
		self.balance += int(n)

	def apply_interest(self):
		self.balance += self.balance * 0.01


def main():
    a1 = CurrentAccount('Joe', 'Murphy', 100)
    a2 = SavingsAccount('Mandy', 'Murray', 100)
    a3 = SavingsAccount('Jimmy', 'Smith', 200)

    # Print base classes
    print('Base classes...')
    print(a1.__class__.__bases__)
    print(a2.__class__.__bases__)

    # Print account details
    print('Account details...')
    print(a1)
    print(a2)
    print(a3)

    # Call some methods
    a1.lodge(50)
    a1.withdraw(100)
    a1.withdraw(100)
    a1.withdraw(1000)
    a2.withdraw(10)
    a2.withdraw(100)
    a2.lodge(20)
    a2.apply_interest()
    try:
        a1.apply_interest()
    except AttributeError:
        print('No such method')

    # Print account details
    print('Account details...')
    print(a1)
    print(a2)

if __name__ == '__main__':
    main()
