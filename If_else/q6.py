try:
    m = int(input("enter"))
    n = 0
    if m > 0:
        n = 1
    elif m < 0:
        n = -1

    print(n)

except:
    print("Enter correct input")

finally:
    print("everytime")

