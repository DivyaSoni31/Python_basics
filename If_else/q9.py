x = int(input("Enter the X coordinaTE"))
y = int(input("y = "))

if x > 0 and y > 0 :
    n = "First"
if x < 0 and y > 0 :
    n = "Second"
if x < 0 and y < 0 :
    n = "Third"
if x > 0 and y < 0 :
    n = "Fourth"
print(f"This is in {n} quadrant")