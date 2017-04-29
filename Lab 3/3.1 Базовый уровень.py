
x = float(input('X: '))
N = int(input('N: '))

y = x**2
a = x
Sum = x
i = 2


for i  in range (N):

    a = -a * y
Sum = Sum + a / (2 * i + 1) 

print('Значение суммы: ' , round(Sum, 3))
