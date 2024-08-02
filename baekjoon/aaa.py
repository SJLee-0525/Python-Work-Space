import sys

M, N = map(int, sys.stdin.readline().rstrip().split())
arr = [[0] * M for _ in range(N)]

T = int(sys.stdin.readline())

for t in range(1, T + 1):
    rc, num = map(int, sys.stdin.readline().rstrip().split())

    if rc == 0: # 가로
        for i in range(N):
            for j in range(M):
                if i < num:
                    arr[i][j] -= t
                else:
                    arr[i][j] += t

    else: # 세로
        for i in range(N):
            for j in range(M):
                if j < num:
                    arr[i][j] -= t
                else:
                    arr[i][j] += t

target_dict = {}
for i in range(N):
    for j in range(M):
        if arr[i][j] not in target_dict:
            target_dict[arr[i][j]] = 1
        else:
            target_dict[arr[i][j]] += 1

count_list = list(target_dict.values())

print(max(count_list))
