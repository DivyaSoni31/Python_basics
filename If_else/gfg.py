N = int(input("Enter:"))
sum=0
while(N>0):
    s=N%10
    sum+=s
    N=N//10  #floor division
    print(N)
print(sum)