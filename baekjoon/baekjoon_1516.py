import sys, heapq
from collections import deque

# 건물이 동시에 지어질 수 있었음 .........

def initSetting():
    for c in range(1, N + 1):
        if not needBuildingsCnt[c]:     # 건설에 선행되는 건물이 없으면
            starts.append(c)            # 시작 건물에 추가하고
            results[c] = needTimes[c]   # 결과 미리 할당

def dijkstra():
    priorityQueue = []
    for start in starts:    # starts 배열을 돌면서 최소힙에 추가
        heapq.heappush(priorityQueue, (needTimes[start], start))

    while priorityQueue:
        currTime, currBuilding = heapq.heappop(priorityQueue)

        if results[currBuilding] > currTime: # 만약 현재 뽑은 시간이 결과 값에 할당된 시간보다 작으면 스킵 (돌 필요 X)
            continue
        for adjBuilding in adjBuildings[currBuilding]:  # 인접 리스트 순회
            needBuildingsCnt[adjBuilding] -= 1          # 순회하면서 건물에 도달할 때마다 건설에 필요한선행 건물 수 감소
            nextTime = results[currBuilding] + needTimes[adjBuilding]
            # 해당 건물 건설에 선행되는 건물이 남아있지 않고, 할당된 결과보다 방금 계산한 소요시간이 더 크다면
            if needBuildingsCnt[adjBuilding] <= 0 and results[adjBuilding] <= nextTime:
                results[adjBuilding] = nextTime # 할당 후 힙에 추가
                heapq.heappush(priorityQueue, (nextTime, adjBuilding))

#######################################################

N = int(sys.stdin.readline())               # 건물의 수

adjBuildings = [[] for _ in range(N + 1)]   # 인접한 빌딩 리스트
needBuildingsCnt = [0] * (N + 1)            # 선행되는 건물 남아있는 수 담을 리스트
needTimes = [0] * (N + 1)                   # 각 건물별 건설에 소요되는 시간

for building in range(1, N + 1):
    needTime, *token = map(int, sys.stdin.readline().split())
    needTimes[building] = needTime
    for i in range(len(token)):
        temp = token[i]
        if temp == -1:
            break
        adjBuildings[temp].append(building) # 인접 리스트에 빌딩 추가 (역으로)
        needBuildingsCnt[building] += 1     # 선행되는 건물 수 추가 (정으로)

# print(needTimes)
# print(adjBuildings)
# print(needBuildingsCnt)

results = [0] * (N + 1) # 결과 겸 visited배열과 유사
starts = []             # 시작할 때
currTime = 0

initSetting()   # starts 배열에 시작 건물들 추가 후
dijkstra()      # 다익스트라 실행

for r in range(1, N + 1):
    print(results[r])