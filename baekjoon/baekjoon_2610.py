from collections import deque
import sys

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA == rootB:
        return
    elif rootA < rootB:
        parents[rootB] = rootA
    else:
        parents[rootA] = rootB

def bfs(startPerson):
    visited = [0] * (N + 1) # 방문 및 관계 거리를 표시할 visited 배열
    visited[startPerson] = 1

    # BFS
    queue = deque([startPerson])
    while queue:
        nowPerson = queue.popleft()
        for adjPerson in adjPersons[nowPerson]:
            # 인접한 사람이 방문 처리된 적이 없고, 같은 부모를 가지고 있다면 방문 처리 및 queue 삽입
            if not visited[adjPerson] and parents[startPerson] == parents[adjPerson]:
                queue.append(adjPerson)
                visited[adjPerson] = visited[nowPerson] + 1

    # 다 순회하면 가장 값이 높은 visited 값을 의사 전달 시간 값으로 할당
    connect_len = max(visited)
    if parents[startPerson] not in tempD:   # 시작한 사람의 조상이 딕셔너리의 KEY에 없다면 추가
        tempD[parents[startPerson]] = (connect_len, startPerson)
    else:  # 있다면 딕셔너리의 VALUE 값에 있는 최대 관계 거리와 비교 후, 더 작다면 새로 할당
        if connect_len < tempD[parents[startPerson]][0]:
            tempD[parents[startPerson]] = (connect_len, startPerson)

    # print(p, visited)

####################################################

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adjPersons = [[] for _ in range(N + 1)] # 관계 인접 리스트
parents = list(range(N + 1))            # parents 배열 초기화

# 양방향 관계 설정과 동시에 두 그룹 합치기
for _ in range(M):
    p1, p2 = map(int, sys.stdin.readline().split())
    adjPersons[p1].append(p2)
    adjPersons[p2].append(p1)
    union(p1, p2)

# 한 번 더 parents 배열 최적화 (안 하니 28%에서 틀림)
for p in range(1, N + 1):
    find(p)

tempD = {}  # 각 그룹의 조상을 KEY로, (거치는 사람의 수, 대표)를 VALUE로 받는 딕셔너리 생성
for p in range(1, N + 1):   # 각 회의의 참석자를 돌면서 bfs 탐색
    bfs(p)

results = []
for value in tempD.values():
    results.append(value[1])

print(len(results))
results.sort() # 작은 순서대로 출력하기 (안 하면 21%에서 틀림)
for result in results:
    print(result)
