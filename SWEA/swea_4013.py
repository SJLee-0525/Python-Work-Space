from collections import deque

def prompt_int(target, prompt):
    '''
    타겟과 명령을 입력받아
    각각의 톱니바퀴 회전 여부와 방향을 만드는 함수
    '''
    prompt_grp = [0, 0, 0, 0]   # 빈 명령 리스트 생성
    prompt_grp[target] = prompt # 입력받은 타겟에 맞는 명령 삽입

    # 타겟 톱니바퀴의 왼쪽을 점검
    std_1 = target      # 기준점 생성 (시작은 타겟으로)
    left = std_1 - 1    # 타겟의 왼쪽 톱니바퀴
    i_prompt_1 = prompt # 타겟의 회전 방향
    while 0 <= left and gears[left][2] != gears[std_1][6]:
        # 마주보는 톱니바퀴의 극성이 다르고 톱니바퀴 인덱스를 벗어나지 않는 선에서
        i_prompt_1 *= -1                # 톱니바퀴 방향은 뒤집고
        prompt_grp[left] = i_prompt_1   # 해당(왼쪽)의 톱니바퀴에 방향에 맞는 명령 삽입
        std_1 = left                    # 기준 톱니바퀴 이동시켜주고
        left = std_1 - 1                # 왼쪽도 다르게 봐줌

    # 타겟 톱니바퀴의 오른쪽을 점검: 위와 같음
    std_2 = target
    right = std_2 + 1
    i_prompt_2 = prompt
    while right <= 3 and gears[std_2][2] != gears[right][6]:
        i_prompt_2 *= -1
        prompt_grp[right] = i_prompt_2
        std_2 += 1
        right = std_2 + 1

    # 만들어진 명령을 회전을 수행하는 함수로 전달 [1, -1, 0, 0]
    rotate_gear(prompt_grp)

def rotate_gear(prompt_grp):
    '''명령을 입력받아 회전을 수행'''
    global gears

    # 톱니바퀴를 순회하며
    for p in range(4):
        if prompt_grp[p] == 1:  # 해당 명령이 시계 방향으로 회전이면
           gears[p].appendleft(gears[p].pop()) # 해당 톱니바퀴 회전

        elif prompt_grp[p] == -1: # 해당 명령이 반시계 방향으로 회전이면
            gears[p].append(gears[p].popleft()) # 해당 톱니바퀴 회전

def cal_score():
    '''점수 계산'''
    score = 0
    for g in range(4):       # 톱니바퀴 순회
        if gears[g][0] == 1: # 만약 12시 방향의 톱니바퀴가 S극이면
            score += 2 ** g  # 점수는 2^톱니바퀴 인덱스와 같음
    return score

T = int(input())
for tc in range(1, T + 1):
    K = int(input()) # 자석을 회전시키는 횟수
    gears = deque()

    # 1: S극 | 2: N극
    # deque([deque([0, 0, 1, 0, 0, 1, 0, 0]), deque([1, 0, 0, 1, 1, 1, 0, 1]), deque([0, 0, 1, 0, 1, 1, 0, 0]), deque([0, 0, 1, 0, 1, 1, 0, 1])])

    # 톱니바퀴 회전이 쉽게끔 deque로 입력받음
    for _ in range(4):
        gears.append(deque(map(int, input().split())))

    # 1: 시계 | -1: 반시계
    for _ in range(K):
        target, prompt = map(int, input().split())
        target -= 1
        prompt_int(target, prompt)

    print(f'#{tc} {cal_score()}')
