ops = ["5","2","C","D","+"]
scores = []

for i in range(len(ops)):
    if ops[i] == "+":
        scores.append((scores[-2]) + (scores[-1]))
    elif ops[i] == "D":
        scores.append((scores[-1]) * 2)
    elif ops[i] == "C":
        scores.pop()
    else:
        scores.append(int(ops[i]))
print(sum(scores))