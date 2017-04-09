import math

x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))
x3 = float(input('x3: '))
y3 = float(input('y3: '))
x4 = float(input('x4: '))
y4 = float(input('y4: '))

A = math.sqrt((x1-x2)**2 + (y1-y2)**2)
B = math.sqrt((x2-x3)**2 + (y2-y3)**2)
C = math.sqrt((x3-x4)**2 + (y3-y4)**2)
D = math.sqrt((x4-x1)**2 + (y4-y1)**2)
P = A + B + C + D

print('P =', P)
