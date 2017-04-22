import math

x0 = float(input('X0: '))
y0 = float(input('Y0: '))
x1 = float(input('X1: '))
y1 = float(input('Y1: '))

A = math.sqrt((x0**2) + (y0**2))
B = math.sqrt((x1**2) + (y1**2))

if A > B:
    print ('Вторая точка наименее удалена')
elif B > A:
    print ('Первая точка наименее удалена')
else:
    print ('Точка находится на одинаковом расстоянии')
