def makeZeros(x,y):
    for i in range(len(matrix)):
        matrix[i][y] = 0
    for j in range(len(matrix[0])):
        matrix[x][j] = 0

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

ans = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            ans.append([i,j])   

for answer in ans:
    makeZeros(answer[0], answer[1])

print(matrix)