import sys

def find(x):
    if parents[x] == x:             # 자기 자신이 부모라면 대표 노드임
        return x
    parents[x] = find(parents[x])   # 경로 압축
    return parents[x]

def union(x, y):
    # 각 노드의 대표 노드 찾기
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:    # 둘이 같은 집합이라면 합칠 필요 X
        return
    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y

def dfs(node):
    stack = [(node, -1)]    # 스택에 (현재 노드, 부모 노드) 저장
    visited[node] = 1       # 방문 처리
    vertexCnt = 0           # 트리의 정점 수 카운트
    edgeCnt = 0             # 트리의 간선 수 카운트

    # DFS
    while stack:
        node, parent = stack.pop()  # 스택에서 현재 노드, 부모 노드 추출
        vertexCnt += 1              # 정점 개수 증가
        for adjNode in adjL[node]:  # 인접 노드 탐색
            edgeCnt += 1            # 간선 개수 증가
            if visited[adjNode] == 0: # 인접 노들르 방문하지 않았다면
                visited[adjNode] = 1  # 방문 처리
                stack.append((adjNode, node)) # 스택에 인접 노드, 현재 노드를 부모 노드로 해 추가
            elif adjNode != parent:     # 다시 방문한 노드가 부모가 아니면 사이클 존재
                return False

    # 트리의 경우, 간선은 (정점 - 1)이어야 함
    # 양방향 간선이므로 간선 수를 2로 나누어 계산
    if edgeCnt // 2 == vertexCnt - 1:
        return True  # 트리임
    else:
        return False # 트리가 아님

#########################################################################
case = 0 # 출력에 테게 있는 거 몰라서 3시간동안 함수 바꾸고 있던 거 실화냐

while 1:
    case += 1

    N, M = map(int, sys.stdin.readline().split()) # 정점 개수, 간선 개수
    if (N, M) == (0, 0):
        break

    parents = list(range(N + 1))        # 부모 배열 초기화
    adjL = [[] for _ in range(N + 1)]   # 인접 리스트 초기화
    visited = [0] * (N + 1)             # 방문 배열 초기화

    # 간선 정보 입력 (양방향으로 처리해야 함. 왜 그런지는 아래 메모에 반례 추가)
    for _ in range(M):
        x, y = map(int, sys.stdin.readline().split())
        union(x, y)         # 입력 받은 두 노드를 합침
        adjL[x].append(y)   # 인접 리스트에 양방향 간선 추가
        adjL[y].append(x)

    used = [0] * (N + 1)    # 사용된 부모 요소를 확인하기 위한 배열
    treeCnt = 0
    for parent in parents[1:]:
        if used[parent]:    # 이미 사용된 부모 노드는 무시
            continue
        used[parent] = 1    # 아니라면 사용 표시 하고
        if dfs(parent):     # 해당 부모 요소로 dfs 탐색, 만약 true가 반환되면 트리로 간주
            treeCnt += 1    # 트리 카운트 증가

    print(f"Case {case}: ", end='')
    if treeCnt == 0:
        print('No trees.')
    elif treeCnt == 1:
        print('There is one tree.')
    else:
        print(f'A forest of {treeCnt} trees.')