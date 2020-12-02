x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[4,5,6],[7,8,9],[0,3,5]]

result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    #print(len(x))
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
print(result)
