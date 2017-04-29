
n = int(input('N: '))
m = int(input('M: '))

s = 0
n += 1

for i in range(1, n):
    multiply = i
    num = i
    for j in range(0, m-1):
        num = num * multiply
        s += num
print(s)






