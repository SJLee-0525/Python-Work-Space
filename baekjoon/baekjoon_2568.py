import sys, bisect

N = int(sys.stdin.readline())

lines = []
for _ in range(N):
    l1, l2 = map(int, sys.stdin.readline().split())
    lines.append((l1, l2))

lines.sort()
# print(lines)

DP = []
store = []
for i in range(N):
    if not DP:
        DP.append(lines[i][1])
    if DP[-1] < lines[i][1]:
        DP.append(lines[i][1])
        store.append((len(DP) - 1, lines[i][1]))
    else:
        idx = bisect.bisect_left(DP, lines[i][1])
        DP[idx] = lines[i][1]
        store.append((idx, lines[i][1]))

print(N - len(DP))

# 필요한 전깃줄 담기
result = []
max_i = len(DP) - 1
for i in range(len(store) - 1, -1, -1):
    if store[i][0] == max_i:
        result.append(store[i][1])
        max_i -= 1

# print(result)

# 필요한 전깃줄들의 A쪽 번호 구하기
A_lines = []
for i in range(N - 1, -1, -1):
    for j in range(len(result)):
        if lines[i][1] == result[j]:
            A_lines.append(lines[i][0])

# print(A_lines)

A_lines.sort()
for i in range(N):
    for j in range(len(A_lines)):
        if lines[i][0] == A_lines[j]: # 만약 필요한 전깃줄이면 중지
            break
    else:
        print(lines[i][0])              # 필요 없는 전깃줄이면 출력