# n = int(input())

# for _ in range(n):
#     x = int(input())

#     while 1:
#         for i in range(2, x + 1):
#             if x == i:
#                 break
#             elif x % i == 0:
#                 x += 1

#         print(x)
#         break


def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1): # 소수를 탐색하는 과정에서 제곱근까지만 탐색해도 됨
        if x % i == 0:
            return False
    return True
        
t = int(input())

for _ in range(t):
    n = int(input())
    
    while 1:
        if prime(n):
            print(n)
            break
        else:
            n += 1