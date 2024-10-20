import sys

H, W = map(int, sys.stdin.readline().split())
ground = list(map(int, sys.stdin.readline().split()))

left_point, right_point = 0, W - 1
left_max, right_max = ground[left_point], ground[right_point]
rain = 0
while left_point < right_point: # 두 포인터가 만나면 종료
    if left_max < right_max:    # 왼쪽의 최대 높이가 오른쪽의 최대 높이보다 낮다면
        left_point += 1         # 왼쪽 포인터 증가
        left_max = max(left_max, ground[left_point]) # 최대값 갱신하고
        if left_max > ground[left_point]:            # 포인터가 바라보는 위치의 블록 높이가 최대 높이보다 낮다면
            rain += left_max - ground[left_point]    # 빗물 카운트

    else:                       # 오른쪽의 최대 높이가 왼쪽의 최대 높이보다 낮다면
        right_point -= 1        # 이하 동일
        right_max = max(right_max, ground[right_point])
        if right_max > ground[right_point]:
            rain += right_max - ground[right_point]

print(rain)