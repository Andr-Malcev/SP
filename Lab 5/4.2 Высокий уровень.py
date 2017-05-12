import random

n = int(input('N: '))

a = [[0] * n for i in range(n)]

for i in range(n):
    a[i][(n - 1) - i] = 1
    for j in range(n - i, n):
        a[i][j] = 2
for row in a:
    print(' '.join([str(elem) for elem in row]))
