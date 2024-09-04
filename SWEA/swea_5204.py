def merge_sort(i_list):
    global cnt
    # 입력받은 리스트의 길이가 1이면 그대로 반환 (정렬할 필요가 없음)
    if len(i_list) == 1:
        return i_list

    mid = len(i_list) // 2   # 리스트를 절반으로 나누기 위해 중간 인덱스 계산
    l = i_list[:mid]         # 절반으로 나눈 리스트의 왼쪽
    r = i_list[mid:]         # 절반으로 나눈 리스트의 오른쪽

    # 재귀를 호출해 나눠진 리스트의 왼쪽 부분과 오른쪽 부분을 정렬
    l = merge_sort(l)
    r = merge_sort(r)

    # 문제 조건: 병합 과정에서 왼쪽 마지막 원소가 오른쪽 원소보다 더 큰 경우 cnt 증가
    if l[-1] > r[-1]:
        cnt += 1

    # 정렬된 각각의 리스트를 병합해서 반환
    return merge(l, r)

def merge(l_list, r_list):
    new_list = [0] * (len(l_list) + len(r_list))     # 병합에 사용할 리스트 생성

    l = 0   # 왼쪽 리스트 탐색할 때 쓸 인덱스
    r = 0   # 오른쪽 리스트 탐색할 때 쓸 인덱스
    while l < len(l_list) and r < len(r_list):  # 한쪽 리스트의 인덱스 값이 같아지거나 높아지기 전까지 반복
        if l_list[l] < r_list[r]:         # 왼쪽 리스트의 인덱스 값이 더 작으면
            new_list[l + r] = l_list[l]   # 결과 리스트의 적정한 위치에 l_list[l] 삽입
            l += 1                        # 왼쪽 리스트 인덱스 값 증가
        else:                             # 오른쪽 리스트의 인덱스 값이 더 작으면
            new_list[l + r] = r_list[r]   # 결과 리스트의 적정한 위치에 r_list[r] 삽입
            r += 1                        # 오른쪽 리스트 인덱스 값 증가

    # 반복을 탈출해도 한쪽에는 아직 삽입하지 않은 값이 남아있음 (한쪽만 다 넣었기에)
    while l < len(l_list):
        new_list[l + r] = l_list[l]
        l += 1

    while r < len(r_list):
        new_list[l + r] = r_list[r]
        r += 1

    return new_list


#################################################################

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 정수 개수
    arr = list(map(int, input().split()))

    cnt = 0
    arr = merge_sort(arr)

    print(f'#{tc} {arr[N//2]} {cnt}')