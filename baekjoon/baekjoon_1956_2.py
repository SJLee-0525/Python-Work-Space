import sys

def floydWarshall():
    '''
    플로이드-워셜:
    모든 정점에서 모든 정점으로 가는 최소 거리 구하기
    '''
    for mid in range(1, V + 1):         # 반드시 경유할 지점
        for start in range(1, V + 1):   # 출발 도시
            for end in range(1, V + 1): # 도착 도시
                # start -> end까지의 거리를 구함: (start -> mid + mid -> end)와 (start -> end) 중 최소 값을 할당
                if arr[start][end] > arr[start][mid] + arr[mid][end]:
                    arr[start][end] = arr[start][mid] + arr[mid][end]

def findCycle():
    '''출발 마을과 도착 마을이 같은 경우의 거리 중 최소 값 구하기'''
    dist = INF                      # 초기 값
    for town in range(1, V + 1):
        if dist > arr[town][town]:   # 최소 값 비교
            dist = arr[town][town]

    if dist == INF:   # 최소 값이 초기 값과 같음: 사이클이 없다
        return -1
    else:                   # 사이클이 있으면 최소 값 반환
        return dist

##################################################################################

V, E = map(int, sys.stdin.readline().split())   # V개의 마을, E개의 도로

INF = float('inf')

# 플로이드-워셜 사전 준비:
arr = [[INF] * (V + 1) for _ in range(V + 1)]         # 2차원 그래프 초기화
for _ in range(E):
    v1, v2, dist = map(int, sys.stdin.readline().split())
    arr[v1][v2] = dist                                      # v1 -> v2 가는 거리 할당 (일방 통행)

# 플로이드-워셜
floydWarshall()

result = findCycle()
print(result)