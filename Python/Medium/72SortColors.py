nums = [2,0,2,1,1,0]

count = 0
i = 0

while True:
    if count >= len(nums)-1:
        break
    count = 0
    for j in range(len(nums) - 1):
        if nums[j] > nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
        else:
            count +=1
    
print(nums)