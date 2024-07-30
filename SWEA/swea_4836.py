T = int(input())

for test_case in range(1, T + 1):
    # 10 * 10인 도화지 만들기
    paper = [[0] * 10 for _ in range(10)]

    N = int(input())
    for paint in range(N):
        # [x_start, y_start] 부터 [x_end, y_end] 까지 color를 더하기 (칠하기)
        x_start, y_start, x_end, y_end, color = map(int, input().split())
        for y in range(y_start, y_end + 1):
            for x in range(x_start, x_end + 1):
                paper[y][x] += color

    # 도화지를 순회하며 purple인 값을 수집
    purple = 0
    for paper_y in range(10):
        for paper_x in range(10):
            if paper[paper_y][paper_x] == 3:
                purple += 1
    
    print(f'#{test_case} {purple}')

# 위 코드는 메모리 에러남