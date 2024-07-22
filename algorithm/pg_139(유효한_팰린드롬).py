'''
주어진 문자열이 팰린드롬인지 확인하라.
대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다
'''

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