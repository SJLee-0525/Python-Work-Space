def quick_sort(left, right):
    if left < right:  # left랑 right가 만나지 않는 동안
        pivot = hoare_partition(left, right)  # 피벗의 위치를 반환받고
        quick_sort(left, pivot - 1)           # 피벗의 왼쪽 부분을 작업영역으로 삼고 재귀
        quick_sort(pivot + 1, right)          # 피벗의 오른쪽 부분을 작업영역으로 삼고 재귀

def hoare_partition(left, right):
    '''
    피봇을 중간 요소로 설정:
    왼쪽이나 오른쪽 요소로 설정하는 것보다 최악의 성능을 보일 확률이 적어
    더 균형 잡힌 성능을 보일 가능성이 큼
    '''
    mid = (left + right) // 2 # 중간 인덱스를 계산해서
    pivot = arr[mid]          # pivot을 중간 요소로 설정

    # 중간 요소를 왼쪽 요소와 교환해서 피벗을 왼쪽으로 이동시킴 (필요시)
    arr[left], arr[mid] = arr[mid], arr[left]

    # 왼쪽, 오른쪽 포인터 초기화 (pivot 이후)
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:   # i가 j를 초과하지 않고, 해당 위치의 값이 피벗보다 작거나 같은 선에서
            i += 1                          # i 증가
        while i <= j and arr[j] >= pivot:   # j가 i 미만으로 내려가지 않고, 해당 위치의 값이 피벗보다 높거나 같은 선에서
            j -= 1                          # j 감소
        if i < j:                           # i가 j보다 작으면 arr[i]와 arr[j] 교환
            arr[i], arr[j] = arr[j], arr[i]

    # 반복문을 탈출하면, 최종적으로 피벗을 배열의 적절한 위치로 이동시키고
    arr[left], arr[j] = arr[j], arr[left]
    return j    # 피벗의 최종 위치를 반환

#################################################################################

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(0, len(arr) - 1)
    print(f'#{tc} {arr[N // 2]}')