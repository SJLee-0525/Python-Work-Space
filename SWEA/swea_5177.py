def enQ(num):
    global last
    last += 1
    HEAP[last] = num    # 힙의 마지막에 원소 추가
    child = last        # 해당 index를 자식 i로
    parent = child // 2 # 부모 index 계산
    while parent >= 1 and HEAP[parent] > HEAP[child]: # 부모 index가 범위를 벗어나지 않고, 부모가 자식보다 큰 동안에는
        HEAP[parent], HEAP[child] = HEAP[child], HEAP[parent]   # 자리를 바꿔서 자식이 부모보다 클 수 있도록 만듦
        child = parent          # 이동 (자식은 부모로)
        parent = child // 2     # 부모 위치 재계산
    # print(HEAP)

def cal_sum(N):
    '''마지막 노드의 부모들의 합을 계산'''
    s = 0
    parent = N // 2 # 마지막 노드의 부모 계산
    while parent >= 1:      # 범위를 벗어나지 않는 선에서
        s += HEAP[parent]   # 변수에 값 추가하고
        parent //= 2        # 부모 위치 변경
    return s

########################################################################

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    seq = list(map(int, input().split()))

    HEAP = [0] * (N + 1)
    last = 0

    for num in seq:
        enQ(num)

    print(f'#{tc} {cal_sum(N)}')