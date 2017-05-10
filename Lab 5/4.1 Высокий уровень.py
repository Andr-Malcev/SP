import numpy as np

a = np.array([int(s,2) for s in input("Массив: ").split()])

np.mean(a)
    

print(sorted(a))
print(np.mean(a))
