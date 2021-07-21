n = int(input("Enter number: "))

if n > 100:
    print("Enter number less than 100")
elif n >= 91:
    print("A+")
elif n >= 81:
    print("A")
elif n >= 71:
    print("B+")
elif n >= 61:
    print("B")
elif n >= 51:
    print("c+")
elif n >= 41:
    print("c")
elif n >= 31:
    print("D")
elif n >= 0 and n <= 30:
    print("Fail")
else: 
    print("Number should be greater than 0")

