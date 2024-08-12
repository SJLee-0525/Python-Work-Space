import sys

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 조합 만들기, (index, 총 수, 나눠지는 요소 수)
def ff(i, N, K): 
    global min_list
    if i == N:
        if sum(b) == K:
            t = [] # b가 1인 경우에 담을 리스트
            f = [] # b가 0인 경우에 담을 리스트 (조합에 없으면)
            for j in range(N):
                if b[j]:    # b가 1이면
                    t.append(a[j])
                else:       # b가 0이면
                    f.append(a[j])
            # print(t, f)
            t_sum = 0 # 조합에 있으면 담을 수
            f_sum = 0 # 조합에 없으면 담을 수
            for ii in range(N//2):
                for jj in range(N//2):
                    if ii != jj: # 둘이 같은 경우는 제외
                        t_sum += arr[t[ii]][t[jj]]  # 어차피 두번씩 들어가게 되므로 한 번만 넣어줘도 됨
                        f_sum += arr[f[ii]][f[jj]]
            min_list.append(abs(t_sum - f_sum))     # 둘의 차이의 절대값을 당믐
    else:
        b[i] = 1
        ff(i + 1, N, K)
        b[i] = 0
        ff(i + 1, N, K)
        

a = list(range(N))  # 조합을 만들어 인덱스에 참조시킬 거임
b = [0] * N         # 조합의 진실 거짓 판단 측정용 리스트
# print(b)

min_list = []
ff(0, N, N//2)

# print(min_list)
print(min(min_list))    # 들어간 차 중 가장 낮은 값을 출력

# di = {}
# for i in range(N):
#     for j in range(i, N):
#         if i != j:
#             di[(i, j)] = arr[i][j] + arr[j][i]
# print(di)
# {(0, 1): 5, (0, 2): 9, (0, 3): 6, (1, 2): 6, (1, 3): 10, (2, 3): 7}
# print('-------------')

# def f(i, N):
#     global min_list
#     if i == N:
#         a_sum = 0
#         b_sum = 0
#         for k in range(N):
#             if k == b[k]:
#                 return
#             if k < N // 2:
#                 a_sum += arr[k][b[k]]
#             else:
#                 b_sum += arr[k][b[k]]
#         print(b)
#         min_list.append(abs(a_sum - b_sum))
            
#         # for k in range(N):
#         #     if b[k]:
#         #         print(arr[k][k], end=' ')
#     for j in range(i, N):
#         b[i], b[j] = b[j], b[i]
#         f(i + 1, N)
#         b[i], b[j] = b[j], b[i]

