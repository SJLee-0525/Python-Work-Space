t = int(input())

for tt in range(t):
    a, b = map(int, input().split())
    if a > b:
        print(f'#{tt + 1} >')
    elif a < b:
        print(f'#{tt + 1} <')
    else:
        print(f'#{tt + 1} =')