import sys, heapq

def dijkstra(start):
    priorityQueue = []
    encounted[start] = 0 # 시작점은 준 여물의 개수가 0
    heapq.heappush(priorityQueue, (0, start)) # (준 여물의 수, 시작점)

    while priorityQueue:
        # 힙큐를 이용해서 가중치가 가장 낮은 정보를 뽑아옴
        curr_encounted, now = heapq.heappop(priorityQueue)

        # 만약 뽑아온 누적 여물의 수가 이미 할당된 것보다 많다면 무시
        if encounted[now] < curr_encounted:
            continue

        # 인접 정보 탐색
        for nextInfo in adjL[now]:
            nextLoc, nextCow = nextInfo
            next_encounted = curr_encounted + nextCow
            # 만약 이미 할당된 다음 헛간의 누적 여물 수보다 현재 계산한 여물의 수가 더 적다면
            if encounted[nextLoc] > next_encounted:
                encounted[nextLoc] = next_encounted # 할당
                heapq.heappush(priorityQueue, (next_encounted, nextLoc)) # 힙큐에 추가

    # print(encounted)
    return encounted[N] # 최종 도착지점의 누적 여물 수 반환

#################################################################

N, M = map(int, sys.stdin.readline().split()) # N개의 헛간, M개의 길

# 인접 리스트 생성
adjL = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2, cows = map(int, sys.stdin.readline().split())
    adjL[v1].append((v2, cows)) # (인접한 헛간, 소의 수) 삽입
    adjL[v2].append((v1, cows))

# 최소 값을 원하니까 누적 여물 리스트에 큰 값을 미리 할당
encounted = [100000001] * (N + 1)

# 항상 1번에서 출발
print(dijkstra(1))