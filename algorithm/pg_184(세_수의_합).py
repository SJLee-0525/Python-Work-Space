# 세 수의 합

# 투포인터로 합 계산
# 브루트 포스는 시간초과 날 가능성이 큼

def threeSum(nums): # 리스트를 받고
    result = []
    nums.sort() # 리스트를 정렬함

    for i in range(len(nums) - 2): # 두 개의 포인터가 뒤에 더 있어야 하기에 2개를 뺌
        if i > 0 and nums[i] == nums[i - 1]: # 중복된 값이 있을 경우 continue로 건너뜀
            continue

        left, right = i + 1, len(nums) - 1 
        # i의 다음 지점과 마지막 지점을 left, right로 설정 후 간격을 좁혀가며 sum을 계산
        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum < 0: # sum이 목표보다 작으면 left를 올려서 값을 키움
                left += 1
            elif sum > 0: # sum이 목표보다 크면 right를 내려서 값을 줄임
                right -= 1
            else: # sum이 목표값인 경우, 이 결과를 result에 추가
                result.append((nums[i], nums[left], nums[right]))
                
                # 추가한 다음 left, right 양쪽으로 동일한 값이 있을 수 있으므로 값이 같은 범위 내에서 스킵할 수 있도록 함
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
                # 어차피 합이 목표값과 동일한 상황임: 하나만 움직여봐야 목표값 안 나오니 두개 다 한 번에 움직임
        
        return result
    
nums = [-1, 0, 1, 2, -1, 4]
print(threeSum(nums))
