import sys

M, N = map(int, sys.stdin.readline().rstrip().split())
arr = [[0] * M for _ in range(N)]

T = int(sys.stdin.readline())

for t in range(1, T + 1):
    rc, num = map(int, sys.stdin.readline().rstrip().split())
    tt = t ** 3 # 회차마다 사용할 식별자. 혹여나 중복을 방지하기 위해 수를 키움

    if rc == 0: # 가로
        for i in range(N):
            for j in range(M):
                if i < num:
                    arr[i][j] -= tt - 1 # 추가적으로 중복 방지 작업 수행
                else:
                    arr[i][j] += tt + 1

    else: # 세로
        for i in range(N):
            for j in range(M):
                if j < num:
                    arr[i][j] -= tt - 1
                else:
                    arr[i][j] += tt + 1

target_dict = {}
for i in range(N):
    for j in range(M):
        if arr[i][j] not in target_dict:
            target_dict[arr[i][j]] = 1
        else:
            target_dict[arr[i][j]] += 1

# print(arr)
count_list = list(target_dict.values())

print(max(count_list))
