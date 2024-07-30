T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 주어지는 배열의 길이
    arr = list(map(int, input().split()))

    # arr 배열에서 max값 찾기
    max_elem = arr[0]
    for elem in arr:
        if max_elem < elem:
            max_elem = elem

    # 카운팅 정렬
    new_arr = [0] * (max_elem + 1)
    for elem in arr:
        new_arr[elem] += 1

    for i in range(1, max_elem + 1):
        new_arr[i] += new_arr[i - 1]
    
    # 카운팅 정렬의 마지막 단계 : 새 리스트에 순서대로 값을 담아 마무리
    sort_arr = [0] * N
    for rev_elem in arr[::-1]:
        sort_arr[new_arr[rev_elem] - 1] = rev_elem ## 카운팅 정렬할 떄 꼭 확인할 것
        new_arr[rev_elem] -= 1

    # 결과를 담을 새 리스트 생성
    result = []
    
    for j in range(5):
        result.append(sort_arr[-1 - j]) # 뒤에서부터 값 추가
        result.append(sort_arr[j]) # 앞에서부터 값 추가
    

    print(f'#{test_case}', end = ' ')
    for result_elem in result:
        print(result_elem, end = ' ')
    print()
    