
x = float(input('X: '))
y = float(input('Y: '))

eps = 0.001

fx = (6*(x**7) - 4.5*(x**5) + 4*(x**2))
if (abs(fx - y) < eps):
    print('Точка B находится на f (x)')
else:
    print('Точка B не находится на f (x)')
