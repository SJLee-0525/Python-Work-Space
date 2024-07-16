def logestPalindrome(s):
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
        
a = 'babas'
print(logestPalindrome(a))

b = 'hellollesas'
print(logestPalindrome(b))