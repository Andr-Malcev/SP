import math

a,p = 5.5,4

b = math.fabs(a) + math.sqrt(a + p**2)
x = math.exp(b)
y = math.cos(x)**3 + math.fabs(a)

print('b =', b)
print('x =', x)
print('y =', y)
