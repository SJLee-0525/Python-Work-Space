import sys

def bellman_ford(start):
    distance = [100000001] * (N + 1) # 최단 거리 테이블 초기화
    distance[start] = 0 # 시작점 초기화

    for i in range(N):      # 전체 N - 1 번의 round를 반복
        for j in range(M * 2 + W):  # 매 반복마다 모든 간선을 확인
            curr_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]

            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            # 문제에서 출발점을 따로 정하지 않았기 떄문에 distance[curr_node] != 100000001 조건을 제거해야 함
            if distance[next_node] > distance[curr_node] + edge_cost:
                distance[next_node] = distance[curr_node] + edge_cost
                if i == N - 1: # N번쨰 라운드에서도 값이 갱신된다면 음수 순환이 존재
                    return True

    return False

##################################################################################

T = int(sys.stdin.readline())
for tc in range(T):
    N, M, W = map(int, sys.stdin.readline().split()) # 지점 수, 도로 수, 웜홀 수

    edges = [] # 모든 간선에 대한 정보를 담는 리스트 생성
    for _ in range(M): # 도로 간선 정보 입력
        s, e, t = map(int, sys.stdin.readline().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(W): # 웜홀 간선 정보 입력
        s, e, t = map(int, sys.stdin.readline().split())
        edges.append((s, e, -t))

    result = bellman_ford(1)
    if result:
        print('YES')
    else:
        print('NO')
