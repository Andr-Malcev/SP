import random

n = 5
m = 5
sum1 = 0

B = [[random.randint(1, 5) for j in range(m)] for i in range(n)]

for row in B:                                                   
    print(' '.join([str(elem) for elem in row]))
for i in range(5):
    for j in range(i+1, 5):
        sum1 += B[i][j]
print('Сумма левой диагонали: ', sum1)

