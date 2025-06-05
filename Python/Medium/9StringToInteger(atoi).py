s = "1337c0d3"
start = False
remember = 1
number = 0

for i in range(len(s)):
    if (start == False):
        if s[i] == " ":
            continue
        elif s[i] == "-":
            remember = -1
            start = True
        elif s[i] == "+":
            start = True
        elif ord(s[i]) >  47 and ord(s[i]) < 58:
            temp = ord(s[i])
            number += (temp - 48) * pow(10 , (len(s) - s.index(s[i]) - 1))
            start = True
        else:
            break
        
    elif (start):
        if ord(s[i]) >  47 and ord(s[i]) < 58:
            temp = ord(s[i])
            number += (temp - 48) * pow(10 , (len(s) - i - 1))
        else:
            number = number // pow(10 , (len(s) - i))
            break

if (2147483647 < number * remember):
    print(2147483647)
elif (2147483648 * remember > number * remember) and remember == -1:
    print(2147483648 * remember)
else:
    print(number * remember)     

   
