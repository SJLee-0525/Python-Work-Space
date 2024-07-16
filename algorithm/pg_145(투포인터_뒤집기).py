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