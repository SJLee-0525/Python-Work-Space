import sys
from collections import deque

# def combi(i, K):
#     if i == K:
#         if sum(B) == 3:
#             temp = []
#             for j in range(K):
#                 if B[j]:
#                     temp.append(empty_list[j])
#             print(temp)
#             return
#     else:
#         B[i] = 1
#         combi(i + 1, K)
#         B[i] = 0
#         combi(i + 1, K)

# def combi_2(K):
#     for i in range(K - 2):
#         for j in range(i, K - 1):
#             if i != j:
#                 for k in range(j, K):
#                     if i != j and j != K:
#                         new_map = [new[:] for new in room]
#                         new_map[empty_list[i][0]][empty_list[i][1]] = 1
#                         new_map[empty_list[j][0]][empty_list[j][1]] = 1
#                         new_map[empty_list[k][0]][empty_list[k][1]] = 1
#                         bfs(new_map)
#                         # print(new_map)

# def combi_3(K):
#     for i in range(1<<K):
#         temp = []
#         for j in range(K):
#             if i & (1<<j):
#                 temp.append(empty_list[j])
#         if len(temp) == 3:
#             new_map = [new[:] for new in room]
#             new_map[temp[0][0]][temp[0][1]] = 1
#             new_map[temp[1][0]][temp[1][1]] = 1
#             new_map[temp[2][0]][temp[2][1]] = 1
#             bfs(new_map)

def combi_4(K):
    bit_N = 2**K - 1

    for i in range(bit_N):
        if bin(i)[2:].count('1') == 3:
            new_map = [new[:] for new in room]
            for j in range(5):
                if i & (1<<j) != 0 :
                    new_map[empty_list[4-j][0]][empty_list[4-j][1]] = 1
            bfs(new_map)


def bfs(input_map):
    global cnt
    Q = deque()
    for vi, vj in virus_list:
        Q.append((vi, vj))

    while Q:
        i, j = Q.popleft()
        input_map[i][j] = 2
        for k in range(4):
            mi, mj = i + di[k], j + dj[k]
            if 0 <= mi < N and 0 <= mj < M and input_map[mi][mj] == 0 and (mi, mj) not in Q:
                Q.append((mi, mj))
    
    c = 0
    for ii in range(N):
        for jj in range(M):
            if input_map[ii][jj] == 0:
                c += 1
    if cnt < c:
        cnt = c


N, M = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

empty_list = []
virus_list = []
for i in range(N):
    for j in range(M):
        if room[i][j] == 0:
            empty_list.append((i, j))
        elif room[i][j] == 2:
            virus_list.append((i, j))

# print(empty_list)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

K = len(empty_list)
cnt = 0
combi_4(K)

print(cnt)