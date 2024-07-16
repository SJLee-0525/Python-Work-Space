def twoSum(nums, target): # 타겟에서 n 값을 뺀 값이 존재하는지 확인하는 방식
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums:
            return [i, nums.index(complement)] # 값이 있는 인덱스를 반환하는 함수임
        
def twoSum_d(nums, target): # 이게 속도가 더 빠름
    nums_dict = {}
    for i, n in enumerate(nums): # 인덱스와 값
        nums_dict[n] = i # 딕셔너리에 값 : 인덱스를 저장
    
    for i, n in enumerate(nums):
        if (target - n) in nums_dict and i != nums_dict[target - n]: 
            # 타겟에서 n을 뺸 값이 딕셔너리의 키에 존재하는지 확인 후 있으면 인덱스 조회
            # 중복 값도 없는지 확인하는 듯? 
            return [i, nums_dict[target - n]]
            # 2번쨰 for문의 인덱스와, 첫번째에서 만든 딕셔너리의 키 값을 반환


nums = [2, 7, 11, 15]
target = 18

print(twoSum(nums, target))
print(twoSum(nums, target))
