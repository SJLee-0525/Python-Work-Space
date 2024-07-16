from collections import deque

def isPalindrome(s):

    strs = deque()
    for char in s:
        if char.isalnum(): # isalnum: 영문자 숫자 여부를 판별하는 함수
            strs.append(char.lower()) # 대소문자 구분을 하지 않는다고 하기에 소문자로 변환

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    
    return True

ss = "A man, a plan, a canal: Panama"
sss = 'race a car'

print(isPalindrome(ss)) # True
print(isPalindrome(sss)) # False