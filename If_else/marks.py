n = int(input("Enter the marks: "))
if n > 100:
    print("Number should be less than 100")
elif n <= 100 and n >= 91:
    print("A+")
elif n <= 90 and n >= 81:
    print("A")
elif n <= 80 and n >= 71:
    print("B+")
elif n <= 70 and n >= 61:
    print("B")
elif n <= 60 and n >= 51:
    print("C+")
elif n <= 50 and n >= 41:
    print("C")
elif n <= 40 and n >= 31:
    print("D")
elif n <= 30 and n >= 0:
    print("FAIL")
else:
    print("Number should be greater than 0.")