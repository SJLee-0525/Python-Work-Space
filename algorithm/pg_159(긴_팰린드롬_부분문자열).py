'''
가장 긴 팰린드롬 부분 문자열을 출력하라
'''
def longestPalindrome(s):
    # 팰린드롬 판별 및 투포인터 확장
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]: 
            # 포인터가 인덱스를 벗어나지 않으면서, 둘이 가르키는 값이 같은 경우에만 포인터 확장
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]: 
        # 해당 사항이 없을 때 빠르게 리턴 (길이가 1 이하거나, 애초에 뒤집었을 때 전체가 팰린드롬이면)
        return s
        
    result = ''

    for i in range(len(s)- 1):
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len) # 이 중에서 길이가 큰 것을 반환하겠다.
    
    return result

def longestPalindrome_2(input_string):
    def expand_2(left, right):
        while left >= 0 and right < len(input_string) and input_string[left] == input_string[right]:
            left -= 1
            right += 1

        return input_string[left + 1:right]

    if len(input_string) < 2 or input_string == input_string[::-1]:
        return input_string
    
    temp_result = ''

    result_list = []
    for i in range(len(input_string) - 1):
        result_list.append(max(temp_result, expand_2(i, i + 1), expand_2(i, i + 2), key=len))

    result = max(result_list, key=len)

    return result

def twoSum_2(nums, target):
    index_dict = {}
    for index, num in enumerate(nums):
        index_dict[num] = index
    
    print(index_dict)
    result = []
    for num in nums:
        if target - num in index_dict:
            result.append(index_dict[target - num])

    return sorted(result)

a = 'babas'
print(longestPalindrome_2(a))

b = 'hellollesas'
print(longestPalindrome_2(b))