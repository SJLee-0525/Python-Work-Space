t = int(input())

for tt in range(t):
    n = int(input())

    if n % 2 == 0:
        print(f'#{tt + 1} {n // -2}')
    elif n % 2 != 0:
        print(f'#{tt + 1} {(n + 1) // 2}')