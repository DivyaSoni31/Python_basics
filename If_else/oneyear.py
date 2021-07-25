'''x = int(input("Date: "))
y = int(input("Month: "))
print(f"{x}:{y}")
sum = 0

if y == 1:
    sum = x
if y == 2:
    sum = 31 + x
if y == 3:
    sum = 31 + 28 + x
if y == 4:
    sum = 31 +28 + 30 + x
if y == 5:
    sum = 2*31 +28 + 30 + x
if y == 6:
    sum = 2*31 +28 + 2*30 + x
if y == 7:
    sum = 3*31 +28 + 2*30 + x
if y == 8:
    sum = 4*31 +28 + 2*30 + x
if y == 9:
    sum = 4*31 +28 + 3*30 + x
if y == 10:
    sum = 5*31 +28 + 3*30 + x
if y == 11:
    sum = 5*31 +28 + 4*30 + x
if y == 12:
    sum = 6*31 +28 + 4*30 + x

    
if sum % 7 == 0:
    print("Tuesday")
if sum % 7 == 1:
    print("Wednesday")
if sum % 7 == 2:
    print("Thursday")
if sum % 7 == 3:
    print("Friday")
if sum % 7 == 4:
    print("Saturday")
if sum % 7 == 5:
    print("sunday")
if sum % 7 == 6:
    print("monday")'''

x = int(input("Date: "))
y = int(input("Month: "))
print(f"{x}:{y}")
sum = 0

if y > 1:
    sum += 31
elif y == 1:
    sum += x

if y > 2:
    sum += 28
elif y == 2:
    sum += x

if y > 3:
    sum += 31
elif y == 3:
    sum += x

if y > 4:
    sum += 30
elif y == 4:
    sum += x

if y > 5:
    sum += 31
elif y == 5:
    sum += x

if y > 6:
    sum += 30
elif y == 6:
    sum += x

if y > 7:
    sum += 31
elif y == 7:
    sum += x

if y > 8:
    sum += 31
elif y == 8:
    sum += x

if y > 9:
    sum += 30
elif y == 9:
    sum += x

if y > 10:
    sum += 31
elif y == 10:
    sum += x

if y > 11:
    sum += 30
elif y == 11:
    sum += x

if y == 12:
    sum += x

if sum % 7 == 0:
    print("Tuesday")
if sum % 7 == 1:
    print("Wednesday")
if sum % 7 == 2:
    print("Thursday")
if sum % 7 == 3:
    print("Friday")
if sum % 7 == 4:
    print("Saturday")
if sum % 7 == 5:
    print("sunday")
if sum % 7 == 6:
    print("monday")