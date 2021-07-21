import math
x = int(input("Date: "))
y = int(input("Month: "))
year = int(input("Year: "))
sum = 0

def ifleap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if y > 1:
    sum +=  31

if y > 2:
    sum +=  28 

if y > 3:
    sum +=  31

if y > 4:
    sum +=  30

if y > 5:
    sum +=  31

if y > 6:
    sum +=  30

if y > 7:
    sum +=  31

if y > 8:
    sum +=  31

if y > 9:
    sum +=  30

if y > 10:
    sum +=  31

if y > 11:
    sum +=  30

sum += x 

if y > 2 and ifleap(year):
    sum += 1


total_year = year - 1
leap4 = math.floor(total_year / 4)
leap100 = math.floor(total_year / 100)
leap400 = math.floor(total_year / 400)
leap = leap4 - leap100 + leap400
non_leap = total_year - leap
days = (non_leap*365 + leap*366)
sum += days


if sum % 7 == 0:
    print("Sunday")
if sum % 7 == 1:
    print("Monday")
if sum % 7 == 2:
    print("Tuesday")
if sum % 7 == 3:
    print("Wednesday")
if sum % 7 == 4:
    print("Thursday")
if sum % 7 == 5:
    print("Friday")
if sum % 7 == 6:
    print("Saturday")