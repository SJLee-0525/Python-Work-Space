import sys

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

def combi_2(K):
    new_map = [new[:] for new in room]
    for i in range(K - 2):
        for j in range(i, K - 1):
            if i != j:
                for k in range(j, K):
                    if i != j and j != K:
                        new_map[empty_list[i][0]][empty_list[i][1]] = 1
                        new_map[empty_list[j][0]][empty_list[j][1]] = 1
                        new_map[empty_list[k][0]][empty_list[k][1]] = 1
                        bfs(new_map)

def bfs(input_map):
    global cnt
    for vi, vj in virus_list:
        for k in range(4):
            mi, mj = vi + di[k], vj + dj[k]
            if 0 <= mi < N and 0 <= mj < M and input_map[mi][mj] == 0:
                while 0 <= mi < N and 0 <= mj < M and input_map[mi][mj] == 0:
                    input_map[mi][mj] = 2
                    mi += di[k]
                    mj += dj[k]

    c = 0
    for i in range(N):
        for j in range(M):
            if input_map[i][j] == 0:
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
# B = [0] * K
# combi(0, K)
combi_2(K)

print(cnt)