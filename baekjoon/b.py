import itertools

N = int(input())
players = [list(map(int, input().split())) for _ in range(N)]

line = list(range(1, 9))  # 0번 타자는 4번 타순에 고정
max_score = 0

for lineup_list in itertools.permutations(line):
    line_up = [lineup_list[0], lineup_list[1], lineup_list[2], 0, lineup_list[3], lineup_list[4], lineup_list[5], lineup_list[6], lineup_list[7]]
    
    t_score = 0
    l = 0
    
    for inning in range(N):
        bases = 0
        out = 0
        while out < 3:
            result = players[inning][line_up[l]]
            
            if result == 0:  # 아웃
                out += 1
            else:
                # 타자 결과에 따라 베이스 상태 계산
                bases = (bases << result) | (1 << (result - 1))
                # 홈에 도착한 주자 점수 추가
                t_score += bin(bases >> 3).count('1')
                bases &= 7  # 3루 이외의 베이스 상태 유지
                
            l = (l + 1) % 9

    max_score = max(max_score, t_score)

print(max_score)