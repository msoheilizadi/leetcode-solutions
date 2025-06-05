def combine(s1 , s2):
    temp = []

    for i in range(len(s1)):
        for j in range(len(s2)):
            temp.append(s1[i] + s2[j])
    return temp

digits = "23"

phoneChar = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
possibleChar = []

for char in digits:
    temp = int(char)
    possibleChar.append(phoneChar[temp - 2])

if len(possibleChar) == 1:
    temp = []
    for char in possibleChar[0]:
        temp.append(char)
    print (temp)
    quit()

while True:
    if len(possibleChar) == 0:
        print([])
        quit()
    if len(possibleChar) <= 1:
        break
    possibleChar[0] = combine(possibleChar[0], possibleChar[1])
    possibleChar.pop(1)

print(possibleChar[0])