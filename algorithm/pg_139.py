from collections import deque

def isPalindrome(s) -> bool:

    strs = deque()
    for char in s:
        if char.isalnum(): # isalnum: 영문자 숫자 여부를 판별하는 함수
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    
    return True

ss = "A man, a plan, a canal: Panama"
# ss = 'race a car'

print(isPalindrome(ss))