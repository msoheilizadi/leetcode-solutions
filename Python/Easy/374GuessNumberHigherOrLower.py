def guess(num):
    if num > pick:
        return -1
    if num == pick:
        return 0
    if num < pick:
        return 1
pick = 3
n = 4

if guess(n) == 0:
    print(n)

Top = n
Low = 1

while True:
    myGuess = (Top + Low) // 2
    apiAnswer = guess(myGuess)
    if apiAnswer == -1:
        Top = myGuess
    elif apiAnswer == 1:
        Low = myGuess
    else:
        break
print(myGuess)