from collections import deque

# def enQueue(item):
#     global rear
#     if not isFull():
#         rear = (rear + 1) % Q_len
#         Q[rear] = item
#
# def deQueue():
#     global front
#     if not isEmpty():
#         front = (front + 1) % Q_len
#         return Q[front]
#
# def isFull():
#     return (rear + 1) % Q_len == front
#
# def isEmpty():
#     return front == rear

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 화덕 크기, 피자 개수
    pizza = list(map(int, input().split()))

    Q = deque() # 화덕
    i = 0
    while i < M:
        if len(Q) < N: # 화덕에 여유공간이 있으면
            Q.append([pizza[i], i]) # [치즈, 피자번호]를 화덕에 추가
        if len(Q) == N: # 만약 꽉 차면
            while 1: # 돌려돌려 치즈 녹이기
                re_pizza = Q.popleft()
                re_pizza[0] //= 2
                if re_pizza[0] != 0: # 만약 덜 녹았으면
                    Q.append(re_pizza) # 다시 넣고
                else:                # 다 녹았으면
                    if i < M - 1:    # 만약 아직 밖에 피자가 더 있다면
                        break        # 중단해서 새 피자 가져옴
                    else:            # 여유 피자가 더 없으면 그냥 계속 돌리는데
                        if len(Q) == 1: # 만약 하나 남으면 중단
                            break
                        continue
        i += 1 # index 추가

    print(f'#{tc} {Q[0][1] + 1}')


    # Q = [0] * (N + 1)
    # Q_len = N + 1
    # front, rear = 0, 0
    # for i in range(N):
    #     judge = isFull()
    #     print(judge)
    #     if judge == False:
    #         enQueue(pizza[i])
    #         print(Q)
    #     elif judge == True:
    #         while 1:
    #             print(Q)
    #             receive_pizza = deQueue()
    #             receive_pizza //= 2
    #             print(rear, front)
    #             if receive_pizza == 0:
    #                 break
    #             else:
    #                 enQueue(receive_pizza)

