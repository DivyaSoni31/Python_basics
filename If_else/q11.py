'''import math
try:
    a = int(input('a = ')) 
    b = int(input('b = '))
    c = int(input('c = '))
    d = (b**2 - 4*a*c)
    x1 = -b + math.sqrt(d) / 2*a
    x2 = -b - math.sqrt(d) / 2*a

    if d > 0:
        y = "Real and Distinct Roots"
    if d == 0:
        y = "Two real and Equal roots"
    if d < 0:
        y = "Roots are imaginary"
    print(y)
except:
    print('imaginary roots')'''

import math

a = int(input('a = ')) 
b = int(input('b = '))
c = int(input('c = '))
d = (b**2 - 4*a*c)


if d >= 0:
    x1 = (-b + math.sqrt(d)) / 2*a
    x2 = (-b - math.sqrt(d)) / 2*a
    if d == 0:
        y = 'Real and equal roots'
        print(x1)
    else:
        y = "Real and Distinct Roots"
        print(x1,x2)
else:
    y = "Roots are imaginary"
    x = -b/2*a  
    z = math.sqrt(-d) /2*a
    x1 = str(x) + ' + ' + 'i' + str(z)
    x2 = str(x) + ' - ' + 'i' + str(z)
    print(x1+"\n"+x2)
print(y)
print('imaginary roots')