g = [1,2,3]
s = [1,2]

s.sort()
g.sort()
j = 0
i = 0
temp = 0

while i != len(s) and j != len(g):
    if s[i] >= g[j]:
        temp += 1
        j += 1
    i += 1
print(temp)