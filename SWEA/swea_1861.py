'''
1. 전체 배열을 순회하면서 확인한다.
2. 인접한 방의 숫자가 현재 방보다 1 크면 visited 1 체크
   -1이 크면 다음으로 갈 수 있다.
     -> 다음으로 갈 수 있는 방이다 라는 정보를 저장
'''

di = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for tc in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    v = [0] * (N * N + 1)

    # 전체를 순회하면서
    # 상하좌우에 나보다 1이 크다면 v체크
    for i in range(N):
        for j in range(N):
            for dx, dy in di:
                ny = i + dy
                nx = j + dx
                # 범위체크
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue
                # 인접이 +1 큰지 체크
                if arr[ny][nx] == arr[i][j] + 1:
                    v[arr[i][j]] = 1
                    # 이미 체크된 순간, 다른 방향은 볼 필요가 없음
                    # 이유 : 동일한 숫자가 없기 때문
                    break
    # cnt : 하나씩 체크/ max_cnt : 정답(최댓값) / start : 계산을 시작할 위치
    cnt = max_cnt = start = 0

    for i in range(N * N - 1, -1, -1):
        print(cnt)
        if v[i]:
            print('index', i)
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1
            cnt = 0  # cnt 초기화

    print(v)
    print(f'#{tc} {start} {max_cnt + 1}')