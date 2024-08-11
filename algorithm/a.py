T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 경로의 길이
    course = list(map(int, input().split()))

    base = 0 # 기준점
    start, end = base, base + 1 # 비교 포인터 할당6
    longest = 0 # 가장 긴 경로를 저장할 변수 할당
    course_len = 1
    min_val = 100000001
    while end <= N: # 종료 조건
        if end >= N and longest == 0:
            longest = course_len
        if end < N and course[start] <= course[end]: # 만약 start에 위치한 값보다 end에 위치한 값이 더 크면
            start += 1 # start와 end 포인터를 하나씩 이동하고 경로 길이 추가
            end += 1
            course_len += 1    
        else: # 만약 start에 위치한 값보다 end에 위치한 값이 더 작으면
            value = (course[end - 1] - course[base]) / course_len # 직전에 쌓아온 정보를 토대로 경사도 측정
            if min_val > value and value != 0: # 만약 경사도가 더 낮다면
                min_val = value # 가장 완만한 경사도 값을 재할당하고 코스 길이 할당
                longest = course_len
            elif min_val == value: # 만약 경사도가 같다면
                if longest < course_len: # 길이가 더 긴 경로를 최장 경로에 할당
                    longest = course_len
            base = end # 기준점을 이동시키고
            start, end = base, base + 1 # 비교 포인터 재할당
            course_len = 1 # 경로 길이 재할당

    print(longest)
    if longest != 1: # 만약 경로값이 한 번이라도 바뀌었다면
        print(f'#{tc} {longest}')
    else: # 바뀌지 않았으면 오르막길이 없었다는 뜻
        print(f'#{tc} 0')

