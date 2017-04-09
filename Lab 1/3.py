import math

m = float(input('m: '))
y = float(input('y: '))

N = (m**2 + 2.8*m + 0.355) / (math.cos(2*y) + 3.6)

print ('N =', N)
