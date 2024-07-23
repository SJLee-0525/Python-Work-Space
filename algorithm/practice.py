# def threeSum(nums, target):
#     result = []
#     for i in range(len(nums)- 2):
#         for j in range(i + 1, len(nums) - 1):
#             for k in range(j + 1, len(nums)):
#                 if nums[i] + nums[j] + nums[k] == target:
#                     result.append([nums[i], nums[j], nums[k]])

#     return result

def threeSum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums)- 2):
        if i > 0 and nums[i] == nums[i - 1]: #### 이게
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] > target:
                right -= 1
            elif nums[i] + nums[left] + nums[right] < target:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                right -= 1
                left += 1
    
    return result



nums = [-1, 0, 1, 2, -1, -4]
target = 0

result = threeSum(nums, target)
print(result)