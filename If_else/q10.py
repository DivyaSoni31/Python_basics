maths = int(input("maths = "))
physics = int(input("physics = "))
chemistry = int(input(" chemistry = "))
x = maths + physics + chemistry
y = maths + physics
flag = 0

if (maths >= 65) and (physics >= 55) and (chemistry >= 55):
    flag = 1

if flag and (x >= 190 or y >= 140):
    print("yes")
else:
    print("no")
               