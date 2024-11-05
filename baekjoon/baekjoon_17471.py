import sys

def combi(lv, cnt):
    '''도시 조합 만들기'''
    global result #

    if lv == N: # 조합이 완성되면 조합대로 선거구 생성
        for city in range(1, N + 1):
            if booleanCheck[city]:
                cityA.append(city)
            else:
                cityB.append(city)

        # 두 선거구 중 하나라도 도시 수가 0이면 성립이 안 되니 중단
        if len(cityA) == 0 or len(cityB) == 0:
            cityA.clear()
            cityB.clear()
            return

        # 선거구별로 탐색 후 인구수 반환 받음
        popA, popB = dfs(cityA[0], cityA), dfs(cityB[0], cityB)

        # 둘 다 돌아지는 경우에 두 선거구의 인구수 차 계산 후 결과랑 비교
        # (반환 값이 0 이상인 경우: 모든 도시가 연결돼 있음)
        if popA >= 0 and popB >= 0:
            temp = abs(popA - popB)
            result = min(result, temp)

        cityA.clear()
        cityB.clear()
        return

    # 체크한 게 도시 수의 절반을 넘어가면, 중단 (중복 방지: [1][2, 3, 4, 5, 6] == [2, 3, 4, 5, 6][1])
    if cnt > N // 2:
        return

    booleanCheck[lv + 1] = 1
    combi(lv + 1, cnt + 1)
    booleanCheck[lv + 1] = 0
    combi(lv + 1, cnt)

def dfs(start, cityList):
    '''완성된 선거구 탐색'''
    stack = []

    # 방문 리스트 생성 후 시작점 방문 처리
    visited = [0] * (N + 1)
    visited[start] = 1

    now = start
    tempPopulation = populations[now] # 인구 수

    # dfs
    while 1:
        for adjCity in adjCities[now]:
            # 만약 인접한 도시를 방문한 적이 없고, 전달받은 선거구의 도시 목록에 해당 도시가 있다면 방문
            if not visited[adjCity] and adjCity in cityList:
                stack.append(now)   # 현위치 스택에 삽입
                now = adjCity       # 이동
                visited[now] = 1    # 방문 처리
                tempPopulation += populations[now] # 인구 수 추가
                break
        else:
            if stack:
                now = stack.pop()
            else:
                # 다 돌았을 때 도시 수랑 방문한 도시 수가 같다면 계산한 인구수 반환
                # (다르면 다 못 돈 것 -> 연결되지 않은 도시가 있다)
                if sum(visited) == len(cityList):
                    return tempPopulation
                else:
                    return -1

###############################################################

N = int(sys.stdin.readline())

populations = [0] + list(map(int, sys.stdin.readline().split()))  # 도시 별 인구 수

# 인접 리스트 생성
adjCities = [[] for _ in range(N + 1)]
for city in range(1, N + 1):
    cnt, *adjInfo = map(int, sys.stdin.readline().split())
    for adjCity in adjInfo:
        adjCities[city].append(adjCity)

cityA, cityB = [], []
booleanCheck = [0] * (N + 1)
result = 100000001
combi(0, 0)

if result == 100000001:
    print(-1)
else:
    print(result)