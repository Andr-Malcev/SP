import math

y = float(input('y: '))
j = float(input('j: '))

F = 2*math.sin(0.354*y+1)/math.log(y+2*j)
     
print('F =', F)
