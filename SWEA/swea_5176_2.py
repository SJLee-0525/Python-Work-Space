def LVR(i, N):
    if i >= N:
        return
    LVR(i * 2 + 1, N) # 인덱스로 하는 것 고려
    temp.append(arr[i])
    LVR(i * 2 + 2, N)

#############################################################

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 일단 순열 만들어서 무작정 돌림
    arr = list(range(1, N + 1))
    temp = []
    LVR(0, N)

    # 딕셔너리 컴프리헨션 이용
    D = {temp[i - 1]:i for i in arr}

    print(f'#{tc} {D[1]} {D[N//2]}')
