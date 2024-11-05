import sys, heapq

def dijkstra(start):
    priorityQueue = []
    distances = [100000001] * (V + 1)
    heapq.heappush(priorityQueue, (0, start))

    while priorityQueue:
        currDist, now = heapq.heappop(priorityQueue)
        if distances[now] < currDist or distances[start] <= currDist:
            continue

        for adjInfo in adjTowns[now]:
            nextTown, nextDist = adjInfo
            distSum = currDist + nextDist
            if distances[nextTown] > distSum:
                distances[nextTown] = distSum
                heapq.heappush(priorityQueue, (distSum, nextTown))

    if distances[start] != 100000001:
        return distances[start]
    else:
        return -1

##################################################################

V, E = map(int, sys.stdin.readline().split()) # V 마을 수 / E 경로 수

adjTowns = [[] for _ in range(V + 1)]
for _ in range(E):
    v1, v2, dist = map(int, sys.stdin.readline().split())
    adjTowns[v1].append((v2, dist))

# print(adjTowns)
result = 100000001
for start in range(1, V + 1):
    temp = dijkstra(start)
    if temp >= 0:
        result = min(result, temp)

if result == 100000001:
    print(-1)
else:
    print(result)
