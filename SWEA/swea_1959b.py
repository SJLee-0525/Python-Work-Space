t = int(input())

for tt in range(t):
    n, m = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    l = []
    if n < m:
        for i in range(m - n + 1):
            temp = []
            for j in range(n):
                k = j + i
                a_temp = A[j] * B[k]
                temp.append(a_temp)
            l.append(sum(temp))
        

    elif n > m:
        for i2 in range(n - m + 1):
            temp2 = []
            for j2 in range(m):
                k2 = j2 + i2
                b_temp = B[j2] * A[k2]
                temp2.append(b_temp)
            l.append(sum(temp2))

    print(f'#{tt + 1} {max(l)}')
