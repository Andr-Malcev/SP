
L = str(input('L: '))

k = 0

for i in range(len(L)):
        if (L[i] == '(') or (L[i] == ')') or (L[i] == '[') or (L[i] == ']'):
                k += 1
print(k)
