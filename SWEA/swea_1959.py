t = int(input())

for test in range(1, t + 1):
    temp_l_2 = []

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n > m:
        a, b = b, a

    for i in range(len(b) - len(a) + 1):
        sum = 0

        for j in range(len(a)):
            sum += a[j] * b[j + i]

        temp_l_2.append(sum)
        max_sum = max(temp_l_2)


    print(f'#{test} {max_sum}')
    