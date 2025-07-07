s = "abc"
t = "ahbgdc"

print("answer")

if len(s) > len(t):
    print(False)
    quit()

lastIndex = 0
count = 0

for i in range(len(s)):
    for j in range(lastIndex, len(t)):
        if t[j] == s[i]:
            count += 1
            lastIndex = j + 1
            break
        elif j == len(t) - 1:
            print(False)
            quit()
if (count == len(s)):
    print(True) 
    quit()