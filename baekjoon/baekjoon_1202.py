'''
각 가방에 담을 수 있는 최대 가치의 보석을 담는데,
용량이 작은 가방부터 담기

보석이 가방에 하나만 들어감!!!1
'''
import sys, heapq

N, K = map(int, sys.stdin.readline().split()) # 보석 수, 가방 수

gems = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split()) # 보석 무게, 가격
    heapq.heappush(gems, (M, V))

bags = []
for _ in range(K):
    bags.append((int(sys.stdin.readline())))
bags.sort() # 가방 크기를 작은 순으로 정렬

result = 0
temp_gems = []
for bag in bags:
    while gems and bag >= gems[0][0]: # 가장 가벼운 보석 무게를 가방이 허용하는 한 반복
        heapq.heappush(temp_gems, -gems[0][1])  # 가격을 최대 힙에 저장
        heapq.heappop(gems)                           # 가격 저장한 보석은 제거

    if temp_gems:  # 가능한 보석 다 저장한 후에, 만약 가능한 보석이 있다면
        result -= heapq.heappop(temp_gems) # 가장 가격이 높은 보석 가격 더하기
    elif not gems: # 더 이상 보석이 없으면 중단
        break

print(result)