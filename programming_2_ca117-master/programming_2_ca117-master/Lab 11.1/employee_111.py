class Employee(object):
	employee_number = 0
	next_employee_number = 1
	def __init__(self, name, surename, ssn):
		self.name = name
		self.surename = surename
		self.ssn = ssn
		Employee.employee_number += 1
		Employee.next_employee_number += 1
		self.number = Employee.employee_number

	def __str__(self):
		return 'Name: {} {}\nSSN: {}\nNumber: {}'.format(self.name, self.surename, self.ssn, self.number)

class SalariedEmployee(Employee):
	tax_rate = 0.2
	def __init__(self, name, surename, ssn, f):
		Employee.__init__(self, name, surename, ssn)
		self.f = f

	def __str__(self):
		return 'Type: Salaried\nName: {} {}\nSSN: {}\nNumber: {}\nEarnings: {:.2f}'.format(self.name, self.surename, self.ssn, self.number, self.f * (1 - SalariedEmployee.tax_rate))


class HourlyEmployee(Employee):
	tax_rate = 0.1
	def __init__(self, name, surename, ssn,f,d):
		Employee.__init__(self, name, surename, ssn)
		self.f = f
		self.d = d

	def __str__(self):
		return 'Type: Hourly\nName: {} {}\nSSN: {}\nNumber: {}\nEarnings: {:.2f}'.format(self.name, self.surename, self.ssn, self.number, (self.f * self.d) * (1 - HourlyEmployee.tax_rate))
	
class CommissionEmployee(Employee):
	tax_rate = 0.05
	def __init__(self, name, surename, ssn, d, f):
		Employee.__init__(self, name, surename, ssn)
		self.f = f
		self.d = d

	def __str__(self):
		return 'Type: Commission\nName: {} {}\nSSN: {}\nNumber: {}\nEarnings: {:.2f}'.format(self.name, self.surename, self.ssn, self.number, (self.d/self.f) * (1 - CommissionEmployee.tax_rate))
	
def main():

	print('Starting number: {}'.format(Employee.next_employee_number))
	print('Tax rate salaried: {:.2f}'.format(SalariedEmployee.tax_rate))
	print('Tax rate hour: {:2f}'.format(HourlyEmployee.tax_rate))
	print('Tax rate commission: {:.2f}'.format(CommissionEmployee.tax_rate))

	e1 = Employee('Danny', 'Willett', '111-11-1111')
	e2 = SalariedEmployee('Jordan', 'Spieth', '222-22-2222', 5000)
	e3 = HourlyEmployee('Lee', 'Westwood', '333-33-3333', 20, 60)
	e4 = CommissionEmployee('Shane', 'Lowry', '444-44-4444', 20000, 10)

	# Print base classes
	print('Base classes...')
	print(e1.__class__.__bases__)
	print(e2.__class__.__bases__)
	print(e3.__class__.__bases__)
	print(e4.__class__.__bases__)

	# Print employee details
	print('Employee details...')
	print(e1)
	print(e2)
	print(e3)
	print(e4)

	print('Ending number: {}'.format(Employee.next_employee_number))

if __name__ == '__main__':
	main()
