nums1 = [1,2,2,1]
nums2 = [2,2]

nums1 = list(set(nums1))
nums2 = list(set(nums2))

numsAns = []

for number1 in nums1:
    if number1 in nums2:
        numsAns.append(number1)
        break

print(numsAns)