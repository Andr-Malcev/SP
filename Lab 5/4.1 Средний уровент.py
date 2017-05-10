import random

R = 3
listA = []
for i in range(10):
    listA.append(round(random.random()*10-5, 2))

print('Исходный массив: ', listA)
print('Наиболее удаленный элемент: ', (max(listA, key=lambda x: abs(R-x))))
