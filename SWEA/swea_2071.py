t = int(input())

for tt in range(t):
    n_list = list(map(int, input().split()))
    print(n_list)
    average_n_list = sum(n_list) / len(n_list)
    print(f'#{tt + 1} {round(average_n_list)}')