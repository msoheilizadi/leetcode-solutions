matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

innerLoop = len(matrix[0])

for i in range(len(matrix) - 1, -1 , -1):
    for j in range(innerLoop):
        matrix[j].append(matrix[i][0])
        matrix[i].pop(0)

print(matrix)