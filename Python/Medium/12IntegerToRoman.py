mainAns = ""
num = 3749

thousand = num // 1000
num -= thousand * 1000

for i in range(thousand):
    mainAns += "M"

hundred = num // 100
num -= hundred * 100

if hundred == 9:
    mainAns += "CM"
elif hundred == 4:
    mainAns += "CD"
else:
    if hundred >= 5:
        mainAns += "D"
        hundred -= 5
    for i in range(hundred):
        mainAns += "C"

ten = num // 10
num -= ten * 10

if ten == 9:
    mainAns += "XC"
elif ten == 4:
    mainAns += "XL"
else:
    if ten >= 5:
        mainAns += "L"
        ten -= 5
    for i in range(ten):
        mainAns += "X"

if num == 9:
    mainAns += "IX"
elif num == 4:
    mainAns += "IV"
else:
    if num >= 5:
        mainAns += "V"
        num -= 5
    for i in range(num):
        mainAns += "I"

print(mainAns)