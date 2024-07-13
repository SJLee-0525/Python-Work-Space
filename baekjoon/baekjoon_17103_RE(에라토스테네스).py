# def prime(a):
#     if a == 0 or a == 1:
#         return False
#     for i in range(2, int(a ** 0.5) + 1):
#         if a % i == 0:
#             return False
#     return True

sosu_list = [False] * 2 + [True] * 999999
for i in range(2, 1001): # prime 범위의 제곱근 (만약 10000까지면 100 + 1) int(1000001 ** 0.5) + 1 도 괜찮은 방법
    if sosu_list[i]:
        for j in range(i * 2, len(sosu_list), i): # 소수 자기 자신을 제외한 배수들을 False로 바꾸어 나가는 과정
            sosu_list[j] = False

t = int(input())

for _ in range(t):
    n = int(input())

    c = 0
    for i in range(2, n // 2 + 1): # 중복되지 않도록 n의 절반만큼만 탐색함
        if sosu_list[i] and sosu_list[n - i]:
            c += 1

    print(c)

