import sys
import heapq

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dijkstra(si, sj):
    priority_queue = []
    lost_rupees[si][sj] = arr[si][sj] # 시작 노드는 시작점에 있는 도둑 루피의 값으로 할당
    heapq.heappush(priority_queue, (arr[si][sj], si, sj)) # 힙큐는 맨 앞의 데이터로 정렬되니까, 루피를 맨 앞에

    while priority_queue:
        cur_lost, i, j = heapq.heappop(priority_queue) # 힙큐에서 데이터 뽑아옴
        if cur_lost > lost_rupees[i][j]: # 현재 위치가 이미 처리 됐다면 (금액이 더 낮다면) 스킵
            continue

        for k in range(4): # 델타 순회
            mi, mj = i + di[k], j + dj[k]
            # 범위를 벗어나지 않고, 다음 위치를 가는데 잃는 돈이 더 적다면 이동
            if 0 <= mi < N and 0 <= mj < N and lost_rupees[mi][mj] > cur_lost + arr[mi][mj]:
                new_lost = cur_lost + arr[mi][mj]   # 잃는 돈 계산하고
                lost_rupees[mi][mj] = new_lost      # 해당 위치에 할당
                heapq.heappush(priority_queue, (new_lost, mi, mj))  # 힙큐에 추가

case = 0
while 1:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    lost_rupees = [[100000001] * N for _ in range(N)]   # 잃는 돈 저장할 배열(visited와 유사한 역할)

    dijkstra(0, 0)

    case += 1
    print(f'Problem {case}: ', end='')
    print(lost_rupees[N - 1][N - 1])

