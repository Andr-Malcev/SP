
n = int(input('N: '))
x = int(input('X: '))

i = 1
sum = 0

while (i <= n):
    sum = ((x**(2*i))/(2*n-1)*(2*n+1)) + sum
    i = i + 1
print('Сумма ',n,' членов ряда равна ',sum)
