import sys

def cal():
    DP = [[0] * i for i in range(1, N + 1)] # 정수 삼각형과 같은 모양의 배열 생성
    DP[0] = arr[0]          # 초기 값 할당

    for i in range(1, N):   # 두번째 층부터 탐색
        for j in range(i + 1):  # 층이 내려갈 수록 정수 삼각형의 배열 너비가 커지니까 범위를 i + 1로 할당
            left = right = 0    # 윗 층의 좌/우 요소 초기 값 설정 (없을 수도 있으니까)
            if j - 1 >= 0:              # 만약 윗층에 왼쪽 요소가 있으면
                left = DP[i - 1][j - 1] # left 요소에 해당 값 할당
            if j < i:                   # 만약 윗층에 오른쪽 요소가 있으면
                right = DP[i - 1][j]    # right 요소에 해당 값 재할당
            DP[i][j] = max(left, right) + arr[i][j] # 둘 중 큰 값을 기준 위치에 저장

    return max(DP[N - 1])   # 마지막 층에서 가장 큰 값 return

#######################################################################

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(cal())