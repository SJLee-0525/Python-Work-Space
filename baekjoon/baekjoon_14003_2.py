import sys, heapq

def dijkstra(start):
    global result

    needTimes = [100000001] * (N + 1)

    priorityQueue = []
    heapq.heappush(priorityQueue, (0, start))

    while priorityQueue:
        currTime, currLoc = heapq.heappop(priorityQueue)
        if needTimes[currLoc] < currTime:
            continue

        for nextLoc, nextTime in adjLocs[currLoc]:
            needTime = currTime + nextTime
            if nextLoc == start and needTime < 0:
                result = 'YES'
                return
            if needTimes[nextLoc] > needTime:
                needTimes[nextLoc] = needTime
                heapq.heappush(priorityQueue, (needTime, nextLoc))



T = int(sys.stdin.readline())
for tc in range(1, T + 1):
    N, M, W = map(int, sys.stdin.readline().split()) # 지점 수, 도로 수, 웜홀 수

    adjLocs = [[] for _ in range(N + 1)]
    for _ in range(M):
        n1, n2, time = map(int, sys.stdin.readline().split())
        adjLocs[n1].append((n2, time))
        adjLocs[n2].append((n1, time))

    for _ in range(W):
        n1, n2, time = map(int, sys.stdin.readline().split())
        adjLocs[n1].append((n2, -time))

    result = 'NO'
    for start in range(1, N + 1):
        if result == 'YES':
            break
        dijkstra(start)

    print(result)