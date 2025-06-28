"""
n = 5
i = 1
ans = False

while True:
    temp = i * i * i * i
    if temp == n:
        ans = True
        break
    elif temp > n:
        break
    i += 1
print(ans)
"""

import math

n = 15

if n <= 0:
    print(False)

x = math.log(n, 4)



print(int(x)  == x)

print(x)