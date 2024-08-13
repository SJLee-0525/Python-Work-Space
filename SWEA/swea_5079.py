T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 길이, 작업 횟수
    arr = list(input().split())
    t = M % N
    print(f'{tc} {arr[t]}')


