s = "ABCD"
numRows = 2

ans = []
index = 0
goBack = False

for i in range(numRows):
    ans.append([])

for char in s:
    ans[index].append(char)
    if goBack:
        index -= 1
    else:
        index += 1
    if index == numRows:
        goBack = True
        index -= 2
    elif index == 0 and goBack:
        goBack = False
    if index < -1:
        index = 0

ansString = ""

for i in range(len(ans)):
    for j in range(len(ans[i])):
        ansString += (ans[i][j])
print(ansString)