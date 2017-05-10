import random

n = int(input('N: '))
sum1 = 0

a = [[random.randint(1, 2) for j in range(n)] for i in range(n)]
for row in a:                                                   
    print(' '.join([str(elem) for elem in row]))
for i in range(n):
        sum1 += a[i][n-1]
print('Сумма последнего столбца: ', sum1)
