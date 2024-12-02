'''
간선 가중치 정보가 없기에, 모든 별들 간의 거리를 재서 인접 리스트에 넣어줘야 함
'''

import sys, heapq

def prim():
    heap = [(0, 0)]     # 0번 별에서 가중치 0으로 시작
    visited = [0] * N   # 방문 리스트

    sumWeight = 0       # 최소 가중치 합계

    while heap:
        currWeight, currStar = heapq.heappop(heap) # 최소힙에서 가장 낮은 거리를 가진 별 정보 꺼내옴
        if visited[currStar]: # 방문한 적 있으면 통과
            continue

        visited[currStar] = 1   # 방문 표시
        sumWeight += currWeight # 가중치 추가

        for nextStar in adjStars[currStar]: # 해당 별에서 인접한 별들을 탐색
            if visited[nextStar[0]]:        # 방문한 적 있으면 스킵
                continue
            # 방문한 적 없는 별의 가중치와 별 위치 정보 담음
            heapq.heappush(heap, (nextStar[1], nextStar[0]))

    return sumWeight

##########################################################

N = int(sys.stdin.readline()) # 별 개수

stars = []          # 별 좌표를 담을 리스트
for _ in range(N):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x, y))

adjStars = [[] for _ in range(N)] # 별들간 인접한 정보를 담을 인접 리스트
for s1 in range(N):
    for s2 in range(N):
        if s1 == s2: # 자기 자신이면 스킵
            continue
        adjStars[s1].append((s2, ((stars[s1][0] - stars[s2][0]) ** 2 + (stars[s1][1] - stars[s2][1]) ** 2) ** 0.5))
        # (상대 별, 상대 별과의 거리)

print(prim())