def f(i, V, C): # V개의 집합에서 i 원소의 포함여부 결정
    if i == V: # 모든 원소에 대해 결정하면
        for i in range(V):
            c = 0
            if b[i]:
                c += 1
                print(arr[i], end=' ')
        print()
    else:
        b[i] = 1        # a[i] 원소가 부분집합에 포함
        f(i + 1, V)     # 다음 원소를 찾으러 가봐
        b[i] = 0        # a[i] 원소가 부분집합에 포함되지 않음
        f(i + 1, V)

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split()) # N 원소의 수 K 집합의 합
    arr = list(range(1, 7))
    b = [0] * 6 

    # 재ㅔ귀로 모든 부분집합 만들기
    f(0, 6, 5) 