x = int(input("first side "))
y = int(input("second side "))
z = int(input("first side "))

if x == y and z == x and y == z:
    d = "Equlateral"
if x == y != z or x != y == z or x == z != y:
    d = "isoscales"
elif x!=y and y!=z and z!=x:
    d = "Scalene"
print(f"triangle is {d}")