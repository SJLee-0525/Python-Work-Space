T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    # n = 정사각형 배열의 길이, m = 회문의 길이
    arr = [list((input())) for _ in range(n)]

    # 기준점 잡기
    for i in range(n - m + 1):
        for j in range(n):
            temp_row = []
            temp_col = []
            for k in range(m):
            # 세로 검사 기준점
                temp_col.append(arr[i + k][j])
            # 가로 검사 기준점
                temp_row.append(arr[j][i + k])
            # append를 안 쓰고 찾는 법을 찾아보자..
            # 뒤집은 거랑 원본이랑 같으면 출력후 브렠         
            if temp_row == temp_row[::-1]:
                result = ''.join(temp_row)
                print(f'#{test_case} {result}')
                break
            elif temp_col == temp_col[::-1]:
                result = ''.join(temp_col)
                print(f'#{test_case} {result}')
                break
            