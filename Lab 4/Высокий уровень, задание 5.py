
s = str(input('S: '))

s2 = ''

for i in range(len(s)):
    if s[i] == '!':
        s2 += str(i)
    else:
        s2 += s[i]
print(s2)


