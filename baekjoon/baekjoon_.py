from collections import deque
import sys
import itertools

N = int(sys.stdin.readline())

players = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

line = list(range(1, 9))
lineup_lists = list(itertools.permutations(line, 8))

max_score = -1
score_list = []
for lineup_list in lineup_lists:
    line_up = [*lineup_list[0:3]] + [0] + [*lineup_list[3:]]
    # print(line_up) # [1, 2, 3, 0, 4, 5, 6, 8, 7]

    t_score = 0
    inning = 0
    out = 0
    status = deque([0, 0, 0])
    l = 0
    while inning < N:
        if players[inning][line_up[l]] == 0:
            out += 1
            if out == 3:
                out = 0
                inning += 1
                status = deque([0, 0, 0])
        elif players[inning][line_up[l]] == 1:
            status.append(1)
            t_score += status.popleft()
        elif players[inning][line_up[l]] == 2:
            status.append(1)
            status.append(0)
            t_score += status.popleft()
            t_score += status.popleft()
        elif players[inning][line_up[l]] == 3:
            status.append(1)
            status.append(0)
            status.append(0)
            t_score += status.popleft()
            t_score += status.popleft()
            t_score += status.popleft()
        elif players[inning][line_up[l]] == 4:
            t_score += sum(status) + 1
            status = deque([0, 0, 0])
        l = (l + 1) % 9
    if max_score < t_score:
        max_score = t_score

print(max_score)
    


# c = []
# for i in range(1<<8):
#     temp = []
#     for j in range(8):
#         if i & (1<<j):
#             print(arr[j], end=' ')
#     print()
