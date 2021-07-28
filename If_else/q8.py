x = int(input())
y = int(input())
z = int(input())
a = int(input())

#Minimum element
"""
def min(a,b):
    if a < b:
        return a
    else:
        return b

print(min(min(x,y),min(z,a)))"""

if x < y:
    min1 = x
else:
    
    min1 = y

if z < a :
    min2 = z
else:
    min2 = a

if min1 < min2:
    print(min1)
else:
    print(min2)