x = int(input('Enter number: '))
if x % 3 == 0 and x % 5 != 0 and x % 7 != 0:  
    print('Yes! good to go')
elif x % 3 == 0 and x % 5 == 0 and x % 7 == 0:
    print("yes!")
elif x % 3 != 0 and x % 5 == 0 and x % 7 != 0:
    print("kuch bhi")
elif x % 3 != 0 and x % 5 != 0 and x % 7 == 0:
    print("yup!")
else:
    print("Nah")