x = int(input("enter the height in cm: "))
if x <= 150:
    x = "drawf"
elif x >= 151 and x <= 190:
    x = "normal"
else:
    x = "Giant"
print(f"Person is {x }" )