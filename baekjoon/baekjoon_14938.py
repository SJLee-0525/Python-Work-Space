import sys
import heapq

def dijkstra(start):
    global result

    dist = [10000001] * (N + 1)
    items = [0] * (N + 1)
    items[start] = itemList[start]
    priorityQueue = []
    heapq.heappush(priorityQueue, (0, items[start], start))
    itemCnt = itemList[start]

    while priorityQueue:
        curr_dist, curr_item, curr_place = heapq.heappop(priorityQueue)
        for next_info in adjL[curr_place]:
            next_place, next_dist = next_info
            new_dist = curr_dist + next_dist
            new_item = curr_item + itemList[next_place]
            if new_dist <= M and new_dist < dist[next_place] and new_item >= items[next_place]:
                items[next_place] = new_item
                dist[next_place] = new_dist
                itemCnt += itemList[next_place]
                heapq.heappush(priorityQueue, (new_dist, new_item, next_place))

    # print(items)
    if result < itemCnt:
        result = itemCnt

#################################################################################

N, M, R = map(int, sys.stdin.readline().split()) # 지역 개수, 수색 범위, 길의 개수
itemList = [0] + list(map(int, sys.stdin.readline().split()))

adjL = [[] for _ in range(N + 1)]
for _ in range(R):
    a, b, l = map(int, sys.stdin.readline().split())
    adjL[a].append((b, l))
    adjL[b].append((a, l))

result = 0

for start in range(1, N + 1):
    dijkstra(start)

print(result)