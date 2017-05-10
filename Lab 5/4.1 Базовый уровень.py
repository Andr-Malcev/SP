from random import uniform

listA = []
listB = []

for i in range(14):
    listA.append(round(uniform(1, 7)))
for j in range(14):
    listB.append(round(uniform(8, 14)))

print(sorted(listA, reverse=False))
print(sorted(listB, reverse=True))
