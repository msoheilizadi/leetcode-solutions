nums = [0,1,0,1,0,1,99]

numsSet = list(set(nums))

for number in numsSet:
    nums.remove(number)
    if number not in nums:
        print(number)
        quit()