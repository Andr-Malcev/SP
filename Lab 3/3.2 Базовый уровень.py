
n=int(input('Введите натуральное число n: '))

for i in range(2, n-1):
    if (n % i == 1):
        print(i)
