numbers = [2,7,11,15]
target = 9

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(i+1)
            print(j+1)
            quit()
        if numbers[i] + numbers[j] > target:
            break
    