matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

for i in range(len(matrix)):
    if target <= matrix[i][-1] and target >= matrix[i][0]:
        for number in matrix[i]:
            if target == number:
                print(True)
                quit()
            if target < number:
                print(False)
                quit()
print(False)