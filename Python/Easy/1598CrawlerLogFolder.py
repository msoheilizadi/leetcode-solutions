logs = ["d1/","d2/","../","d21/","./"]
ans = 0

for char in logs:
    if char == "../":
        ans -= 1
        if ans < 0:
            ans = 0
    elif char == "./":
        continue
    else:
        ans += 1

print(ans) 