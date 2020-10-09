class File(object):
	FILE_PERMISSIONS = 'rwx'
	def __init__(self, fille, name, size=0, per=None):
		self.file = fille
		self.name = name
		self.size = size
		if per == None:
			self.per = 'null'
		else:
			self.per = per

	def __str__(self):
		return 'File: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes'.format(self.file, self.name, self.per, self.size)

	def has_access(self, name, per):
		if name == self.name:
			return 'Access granted'
		else:
			if per in self.per:
				return 'Access granted'
			else:
				return 'Access denied'

	def enable_permission(self, name, per):
		if name == self.name:
			if self.per == 'null':
				if per == 'w' or per == 'r' or per == 'x':
					self.per = per
			else:
				if not per in self.per:
					if per == 'w' or per == 'r' or per == 'x':
						self.per += per
		else:
			print('Access denied')
					
	def get_permissions(self):
		return ''.join(sorted(self.per))

	def disable_permission(self, name, per):
		if name == self.name:
			k = self.per
			self.per = k.replace(per, '')
		else:
			print('Access denied')

class Folder(object):
	f_size = 0
	def __init__(self, d=None):
		if d == None:
			self.d = {}
		else:
			self.d = {}

	def add_file(self, other):
		if not other.file in self.d:
			self.d[other.file] = other.size,other.name,other.per
			Folder.f_size += other.size
		else:
			print('File already exists')

	def del_file(self, name, fille):
		if fille in self.d:
			if self.d[fille][1] == name:
				Folder.f_size -= self.d[fille][0]
				del self.d[fille]
			else:
				print('Access denied')
		else:
			print('No such file')

	def __str__(self):
		print('Folder contents\n===============')
		opt = ''
		for i in sorted(self.d):
			opt = opt + 'File:' + ' ' + i + '\n' + 'Owner:' + ' ' + self.d[i][1] + '\n' + 'Permissions:' + ' ' + self.d[i][2] + '\n' + 'Size:' + ' ' + str(self.d[i][0]) + ' bytes' + '\n'
		opt = opt  + 'Folder size: ' + str(Folder.f_size) + ' bytes' + '\n'
		return '{}'.format(opt.rstrip('\n'))

def main():

	# Create an empty folder
	print('Initialise empty folder...')
	folder = Folder()

	# Create some files
	print('Initialise some files...')
	f1 = File('poem.txt', 'joe')
	f2 = File('readme.txt', 'max', 1000, 'r')
	f3 = File('secret.txt', 'fred', 100, 'rw')
	f4 = File('exam.txt', 'jim', 3000, 'x')

	# Add files to the folder
	print('Add files to folder...')
	folder.add_file(f1)
	folder.add_file(f2)
	folder.add_file(f3)
	folder.add_file(f4)

	# Try adding same file twice
	print('Add existing file to folder...')
	folder.add_file(f1)

	# Display folder contents
	print('Display folder contents...')
	print(folder)

	# Max tries to delete a file
	print('Max deletes a file...')
	folder.del_file('max', 'readme.txt')

	# Max tries to delete a file
	print('Max deletes a file...')
	folder.del_file('max', 'readme.txt')

	# Joe tries to delete a file
	print('Joe deletes a file...')
	folder.del_file('joe', 'secret.txt')
    
	# Display folder contents
	print('Display folder contents...')
	print(folder)

if __name__ == '__main__':
	main()



