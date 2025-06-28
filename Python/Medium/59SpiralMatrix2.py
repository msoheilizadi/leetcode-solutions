matrix = []
n = 4
temp = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(0)
    matrix.append(temp)


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
number = 1

for _ in range(n * n):
    matrix[i][j] = number


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

    number += 1
    
print(matrix)

