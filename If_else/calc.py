a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter the operation: ")





if c == '+':
    print("Performing addition, pleasee wait...", end="\t")
    d = a + b
    print(d)
elif c == '*': # and c != '+'
    print("Performing multiplication, pleasee wait...", end="\t")
    d = a * b
    print(d)
     
elif c == '-': # and c != '+ and c != '*'
    print("Performing subtraction, pleasee wait...", end="\t")
    d = a - b
    print(d)
elif c == '/':# and c != '+ and c != '*' and c != '-'
    print("Performing division, pleasee wait...", end="\t")
    d = a / b
    print(d)
else: #  c != '+ and c != '*' and c != '-' and c != '/'
    print("invalid")

