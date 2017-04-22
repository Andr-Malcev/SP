
x1 = int(input('X1: '))
y1 = int(input('Y1: '))
x2 = int(input('X2: '))
y2 = int(input('Y2: '))
x3 = int(input('X3: '))
y3 = int(input('Y3: '))
x4 = int(input('X4: '))
y4 = int(input('Y4: '))


if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else: x4 = x1

if y1 == y2:
    y4 = y2
elif y1 == y3:
    y4 = y2
else: y4 = y1
print('Координаты  четвертой вершины: ', x4, ' ', y4)
    
