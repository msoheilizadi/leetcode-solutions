matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrixAns = []

endOfLine = len(matrix[0]) - 1
endOfRow  = len(matrix) - 1
startOfLine = 0
startOfRow = 1

rowNegetive = 0
lineNegetive = 1
rowBackward = False
lineBackward = False

i = 0
j = 0

for _ in range(len(matrix) * len(matrix[i])):
    temp = matrix[i][j]
    matrixAns.append(temp)


    if j == endOfLine and lineBackward == False and lineNegetive != 0:
        rowNegetive = 1
        lineNegetive = 0
        lineBackward = True
        endOfLine -= 1
    elif j == startOfLine and lineBackward == True and lineNegetive != 0:
        rowNegetive = -1
        lineNegetive = 0
        lineBackward = False
        startOfLine += 1
    if i == endOfRow and rowBackward == False and rowNegetive != 0:
        rowNegetive = 0
        lineNegetive = -1
        rowBackward = True
        endOfRow -= 1
    elif i == startOfRow and rowBackward == True and rowNegetive != 0:
        rowNegetive = 0
        lineNegetive = 1
        rowBackward = False
        startOfRow += 1

    i += rowNegetive
    j += lineNegetive
    
print(matrixAns)
