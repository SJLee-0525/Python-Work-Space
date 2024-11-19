import sys

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    elif root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y

################################################################################

N, M = map(int, sys.stdin.readline().split()) # N 국가 수, M 기록 수

parents = list(range(N + 1))
population = [0] * (N + 1)

for _ in range(N):
    O, P, Q = map(int, sys.stdin.readline().split()) # O = 1 : 동맹 / O = 2 : 전쟁
    if O == 1:
        union(P, Q)

