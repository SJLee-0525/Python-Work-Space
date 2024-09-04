def binary_search(l, r, target, check=None):
    global cnt

    m = (l + r) // 2  # 중앙 원소의 인덱스 값 계산

    if check == None:   # 만약 입력받은 check가 없으면 (초기 상태)
        check = [0]     # check 리스트 생성 (시작하자마자 끝나는 경우가 있어서 0 담고 시작)

    if l > r:           # 만약 왼쪽 인덱스가 오른쪽 인덱스를 초과하면 (target이 없음)
        return False    # 함수 중단

    if A[m] == target:  # 만약 중앙 원소의 값이 target과 같으면 (값을 찾음)
        check_target = check[0] # 왼쪽 오른쪽 번갈아가면서 찾았는지 확인하기 위한 초기 값 지정
        print(check, target)
        for c in range(1, len(check)):      # check 리스트 순회
            if check_target != check[c]:    # 만약 check_target이 check[c]와 다르면
                check_target = check[c]     # check_target을 check[c]로 할당하고 다음 반복
            elif check_target == check[c]:  # 만약 check_target과 check[c]가 같으면 (한쪽 방향으로 두 번 탐색했다는 것)
                break                       # 중단
        else:           # 끝까지 다 돌면(끝까지 다른 값들이 나열됨) [0, -1, 1] < 이런식: 왼쪽으로 탐색 후 오른쪽 탐색했다는 뜻
            cnt += 1    # 카운트 증가 후
        return          # 리턴

    elif A[m] > target:     # 만약 중앙 원소 값이 타겟보다 크면
        check.append(-1)    # check에 왼쪽 탐색 했다는 표시 남기고 (-1)
        binary_search(l, m - 1, target, check)  # l, r 재할당해서 왼쪽 탐색

    elif A[m] < target:     # 만약 중앙 원소 값이 타겟보다 작으면
        check.append(1)     # check에 오른쪽 탐색 했다는 표시 남기고 (1)
        binary_search(m + 1, r, target, check)  # l, r 재할당해서 오른쪽 탐색

#######################################################################################

T = int(input())
for tc in range(1, T + 1):
    A_len, B_len = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 테케를 정렬해서 주는지 모르겠어서 일단 정렬 (B는 정렬할 필요 없잖아)
    A.sort()

    cnt = 0
    for target in B: # B를 돌면서 타겟을 뽑아서 이진 탐색
        binary_search(0, A_len - 1, target)

    print(f'#{tc} {cnt}')