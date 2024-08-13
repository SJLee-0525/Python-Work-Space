from collections import deque

# deque 써보기

T = int(input())
for tc in range(1, T + 1):
    N, *switch_info = input().split()

    # 각 로봇들이 가야할 목표 위치를 정리
    target = deque()  # [['B', 2], ['O', 1], ['O', 2], ['B', 4]]
    orange_target = deque() # [1, 2]
    blue_target = deque() # [2, 4]
    for i in range(int(N)):
        target.append([switch_info[i * 2], int(switch_info[i * 2 + 1])])
        if switch_info[i * 2] == 'O':
            orange_target.append(int(switch_info[i * 2 + 1]))
        else:
            blue_target.append(int(switch_info[i * 2 + 1]))

    orange_robot, blue_robot, o_i, b_i, count = 1, 1, 0, 0, 0
    while 1:
        # 만약 타겟들이 다 비워지면 스위치 다 누른 것이므로 중단
        if not orange_target and not blue_target:
            break

        # 매 반복마다 초 추가
        count += 1
        b = True # 동시에 누르지 않게끔 설정하는 변수
        if orange_target: # orange 타겟 리스트에 요소가 하나라도 있다면
            if orange_robot == orange_target[0] and target[0][0] == 'O':
                # 만약 타겟에 도착했고, 눌러야 하는 우선순위가 맞다면
                orange_target.popleft() # 타겟에서 앞의 것을 뺌
                target.popleft()
                b = False # 뒤에 Blue가 스위치 누르는 일이 없게끔 변수 변경
            else: # 만약 타겟과 다르다면
                if orange_robot < orange_target[0]: # 타겟보다 낮으면 올리고
                    orange_robot += 1
                elif orange_robot > orange_target[0]: # 높으면 내림
                    orange_robot -= 1

        # 이하 동일
        if blue_target:
            # b == True만 추가 (True라면 앞에서 스위치를 안 눌렀을테니)
            if b == True and blue_robot == blue_target[0] and target[0][0] == 'B':
                blue_target.popleft()
                target.popleft()
            else:
                if blue_robot < blue_target[0]:
                    blue_robot += 1
                elif blue_robot > blue_target[0]:
                    blue_robot -= 1
    print(f'#{tc} {count}')