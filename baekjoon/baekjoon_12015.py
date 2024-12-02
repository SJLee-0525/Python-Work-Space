'''
N log N LIS 알고리즘 : 이진 탐색

단, 아래 방법으로는 길이밖에 구할 수 없음

1. DP를 배열의 첫번째 요소로 초기화
2. 현재 존재하는 DP의 마지막 요소보다 현재 배열에서 가리키는 요소가 더 크다면 DP의 마지막에 추가
3. 현재 존재하는 DP의 맨 마지막 요소보다 현재 배열에서 가리키는 요소가 더 작거나 같다면, DP에서 현재 위치의 요소가 들어갈 자리를 찾아 대체
'''

import sys, bisect

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

DP = [arr[0]] # DP 초기화

for i in range(1, N):
    if DP[-1] < arr[i]:     # DP 마지막 요소보다 배열에서 가리키는 요소가 더 크면
        DP.append(arr[i])   # DP 마지막에 추가
    else:                   # DP 마지막 요소보다 배열에서 가리키는 요소가 더 크지 않다면
        idx = bisect.bisect_left(DP, arr[i]) # 이진 탐색을 통해서 배열에서 가리키는 요소의 자리를 찾음
        DP[idx] = arr[i]                     # 해당 자리를 현재 가리키는 요소로 대체

print(len(DP))