import sys

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di = {}
for i in range(N):
    for j in range(i, N):
        if i != j:
            di[(i, j)] = arr[i][j] + arr[j][i]
print(di)

for key, value in di.items():
    