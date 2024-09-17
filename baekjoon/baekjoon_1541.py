import sys

'''
55-50+40-50+40-50-50
'''

arr = sys.stdin.readline().rstrip()
numbers = list(arr.split('-')) # 아래와 같이 - 기호로 끊어서 구분
# print("numbers", numbers) # numbers ['55', '50+40', '50+40', '50', '50']

result = sum(list(map(int, numbers[0].split('+')))) # 첫번째 요소의 합을 시작 값으로 설정

if len(numbers) >= 2:   # 분리된 식의 길이가 2 이상이라면 (1이라면 index에러 남)
    for nums in numbers[1:]:
        temp = sum(list(map(int, nums.split('+')))) # - 로 구분되어 나눠졌으므로, 구분된 것들의 합을
        result -= temp                              # result에서 계속 빼줌

print(result)