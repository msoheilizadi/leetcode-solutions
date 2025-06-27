def countBits2(num):
    ans = 0
    if num == 0:
        return 0
    if num == 1:
        return 1
    while True:
        tempRemain = num // 2
        Reminder = num % 2
        if Reminder == 1:
            ans += 1
        if tempRemain == 2:
            ans += 1
            break
        if tempRemain == 1:
            ans += 1
            break
        num = tempRemain
    return ans
print(countBits2(11))