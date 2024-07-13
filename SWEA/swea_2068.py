t = int(input())

for tt in range(t):
    n_list = list(map(int, input().split()))
    print(f'#{tt + 1} {max(n_list)}')