def order(i):
    if i >= N:  # i가 범위를 벗어나면 재귀 종료
        return
    order((2 * i) + 1)    # 인덱스로 계산했을 때 왼쪽 자식 노드의 i는 이와 같음
    result.append(arr[i]) # 중위 순회
    order((2 * i) + 2)    # 인덱스로 계산했을 때 왼쪽 자식 노드의 i는 이와 같음

##########################################

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 이진 탐색 트리에 들어갈 1 ~ N까지의 자연수
    arr = list(range(1, N + 1)) # [1, 2, 3, 4 ,5, 6] # 자연수 리스트

    result = [] # 방문하게 되는 노드 번호의 순서 [4, 2, 5, 1, 6, 3]
    order(0) # 재귀 호출
    # print(result)

    result_list = [0] * (N + 1) # 인덱스를 이용해서 결과값 저장
    # [0, 4, 2, 6, 1, 3, 5]

    for i, r in enumerate(result):  # i = 자연수, r = 노드 번호
        result_list[r] = i + 1      # 해당 노드 번호의 위치에 자연수 삽입

    print(f'#{tc} {result_list[1]} {result_list[N // 2]}')
    # 1번 위치의 자료와 N//2번째 위치의 자료 출력