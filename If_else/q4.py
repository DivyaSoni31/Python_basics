def isLeap (N):
    if N % 4 == 0:
        if N % 100 == 0:
            if N % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

x = int(input("Enter year"))
y = isLeap(x)

if y == 0:
    print("Not a leap year")
else:
    print("Leap year")

