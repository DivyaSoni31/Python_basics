n = int(input())
for i in range(n):
    p = input()
    if len(p) > 10:
        print(p[0] + str(len(p) - 2) + p[-1])
    else:
        print(p)
    


