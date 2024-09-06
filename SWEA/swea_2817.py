def make_sum(lv, s, N):
    global count
    if lv == N:
        if s == K:
            count += 1
        return
    if s > K:
        return

    used[lv] = 1
    make_sum(lv + 1, s + arr[lv], N)
    used[lv] = 0
    make_sum(lv + 1, s, N)


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())  # N개의 자연수  | 합이 K
    arr = list(map(int, input().split()))

    used = [0] * N
    count = 0

    make_sum(0, 0, N)

    print(f'#{tc} {count}')