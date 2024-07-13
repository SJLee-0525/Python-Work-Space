t = int(input())

for tt in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()

    print(f'#{tt + 1}', end = ' ')
    print(*l)