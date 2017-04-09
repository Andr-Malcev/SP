import math

y = float(input('y: '))

H = math.sin(y**2) - 2.8*y + math.sqrt(abs(y))

print ('H = ', H)
