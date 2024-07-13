t = int(input())

for tt in range(t):
    a, b = map(int, input().split())
    if a + b >= 24:
        print(f'#{tt + 1} {(a + b) % 24}')
    else:
        print(f'#{tt + 1} {a + b}')