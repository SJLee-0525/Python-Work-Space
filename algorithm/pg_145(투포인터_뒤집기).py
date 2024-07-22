'''
문자열을 뒤집는 함수를 작성하라.
입력 값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라
'''
# 투포인터로 뒤집기

def twopointer(s): 
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

s = list('hello')

result = twopointer(s)

print(result)

# reverse() 함수를 사용해도 빠르니 그거 사용해도 됨