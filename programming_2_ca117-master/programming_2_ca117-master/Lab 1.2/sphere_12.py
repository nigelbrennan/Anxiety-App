import math
from math import pi
import sys

start = float(sys.argv[1])
step = float(sys.argv[2])
stop = float(sys.argv[3])
r = 'Radius (m)'
a = 'Area (m^2)'
v = 'Volume (m^3)'

print('{:>10s} {:>15s} {:>15s}'.format(str(r), str(a), str(v)))

print ('----------      ----------    ------------')

while start < (stop + step):
	print('{:10.1f} {:15.2f} {:15.2f}'.format(float(start), 4*pi*float(start)**2, (4/3)*pi*(float(start)**3)))
	start += step
	
