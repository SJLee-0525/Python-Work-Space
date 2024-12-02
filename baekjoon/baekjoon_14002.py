import sys
from collections import deque

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

DP = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            DP[i] = max(DP[i], DP[j] + 1)

max_dp = max(DP)
print(max_dp)

max_i = DP.index(max_dp)
queue = deque()

while max_i >= 0:
    if DP[max_i] == max_dp:
        queue.appendleft(arr[max_i])
        max_dp -= 1
    max_i -= 1

result = ''
for q in queue:
    result += str(q) + ' '

print(result)
