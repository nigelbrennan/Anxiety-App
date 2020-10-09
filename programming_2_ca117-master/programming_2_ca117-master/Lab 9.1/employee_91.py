class Manager(object):
	def __init__(self, name, no, salary):
		self.no = no
		self.salary = salary
		self.name = name

	def __str__(self):
		return 'Name: {}\nNumber: {}\nWages: {:.2f}'.format(self.name, self.no, self.salary / 52)

class AssemblyWorker(object):
	def __init__(self, name, no, salary=0, hours=0):
		self.no = no
		self.salary = salary
		self.name = name
		self.hours = hours

	def __str__(self):
		return 'Name: {}\nNumber: {}\nWages: {:.2f}'.format(self.name, self.no, self.salary * self.hours)

class Employee(object):
	def __init__(self, name, no, salary=0, hours=0):
		self.no = no
		self.salary = salary
		self.name = name
		self.hours = hours

	def __str__(self):
		return 'Name: {}\nNumber: {}\nWages: {:.2f}'.format(self.name, self.no, self.salary * self.hours)


def main():

    e1 = Manager('Mary', 1, 50000)
    e2 = AssemblyWorker('Fred', 2, 15.50, 40)
    e3 = Employee('Sean', 3)

    print(e1)
    print(e2)
    print(e3)

if __name__ == '__main__':
    main()
