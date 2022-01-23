x1 = int(input('Digite o primeiro número inteiro'))
y1 = int(input('Digite o primeiro número inteiro'))
x2 = int(input('Digite o primeiro número inteiro'))
y2 = int(input('Digite o primeiro número inteiro'))

import math

D = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if D >= 10:
    print('longe')
else:
    print('perto')

        