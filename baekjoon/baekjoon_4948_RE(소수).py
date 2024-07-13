def prime(a):
    if a == 0 or a == 1:
        return False
    for b in range(2, int(a ** 0.5) + 1):
        if a % b == 0:
            return False
    return True

# while 1:
#     n = int(input())

#     if n == 0:
#         break

#     c = 0
#     for i in range(n + 1, (2 * n) + 1):
#         if prime(i):
#             c += 1
    
#     print(c)
    
''' 위는 맞았으나 시간 초과된 풀이 '''


all_list = list(range(2, 123456 * 2)) # 시간 단축을 위해 미리 소수 리스트를 만드는 과정
memo = []

for i in all_list:
    if prime(i):
        memo.append(i)


while 1:
    n = int(input())
    c = 0

    if n == 0:
        break
    for i in memo:
        if n < i <= 2 * n:
            c += 1
    print(c)

