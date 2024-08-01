def binary_search(page, target):
    start, end = 0, page
    count = 0
    while start <= end:
        mid = (start + end) // 2
        if target == mid:
            return count
        elif target > mid:
            start = mid + 1
            count += 1
        elif target < mid:
            end = mid - 1
            count += 1

T = int(input())

for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    # P = 전체 쪽수 / A, B = 각자 찾아야 하는 수
    print('A', binary_search((P, A)))
    print('B', binary_search((P, B)))




