import math

k = int(input('K: '))

Y = 0

for n in range(1, k+1):
            Y = Y + ((-1)**(2*n))*((n**2-9)**2)/math.factorial(3*n)
print('Сумма: ', Y)
