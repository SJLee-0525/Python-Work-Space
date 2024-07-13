t = int(input())

for tt in range(t):
    l, u, x = map(int, input().split())
    if x < l:
        print(f'#{tt + 1} {l - x}')
    elif l <= x <= u:
        print(f'#{tt + 1} 0')
    elif x > u:
        print(f'#{tt + 1} -1')