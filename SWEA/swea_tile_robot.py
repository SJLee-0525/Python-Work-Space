for tc in range(1, int(input()) + 1):
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())
    cnt = 0
    for _ in range(N):
        i1, j1, i2, j2 = map(int, input().split())
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                if arr[i][j] == 0:
                    arr[i][j] += 1
                    cnt += 1

    print(f'#{tc} {cnt}')