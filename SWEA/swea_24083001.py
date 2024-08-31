result = ['OFF'] * 10000

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    for i in range(N):
        if not M & (1 << i):
            break
    else:
        result[tc] = 'ON'

for t, val in enumerate(result):
    print(f'#{t + 1} {val}')
