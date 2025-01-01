import sys

def bellmanFord():
    # 거리 정보 배열 생성 및 시작 노드에 한해서 초기화
    dist = [float('inf')] * (N + 1)
    dist[1] = 0

    for round in range(1, N + 1):  # 전체 N번의 round를 반복
        for currCity in range(1, N + 1): # 매 반복마다 모든 간선을 확인함
            for nextCity, needTime in adjCities[currCity]:
                # 현재 간선의 거리가 무한이 아니면서: currCity에 도달할 수 있는 경우에만 확인
                # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if dist[currCity] != float('inf') and dist[nextCity] > dist[currCity] + needTime:
                    dist[nextCity] = dist[currCity] + needTime
                    if round == N: # N번째 라운드에서도 값이 갱신된다면, 음수 순환이 존재
                        print(-1)
                        return

    for city in range(2, N + 1):
        if dist[city] == float('inf'):
            print(-1)
        else:
            print(dist[city])

#############################################################

N, M = map(int, sys.stdin.readline().split())

adjCities = [[] for _ in range(N + 1)]
for _ in range(M):
    c1, c2, t = map(int, sys.stdin.readline().split())
    adjCities[c1].append((c2, t))

bellmanFord()