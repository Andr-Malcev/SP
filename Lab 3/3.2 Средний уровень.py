
s = str(input('S: '))

sum1=int(s[0])+int(s[1])+int(s[2])
sum2=int(s[3])+int(s[4])+int(s[5])
if sum1==sum2:
    if sum1 == 13:
        sum1 = sum1 + 1
    print('Счастливых билетов = ', sum1)
else:
    print('Не счастливый')

