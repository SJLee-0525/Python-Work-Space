# 당신은 택시 기사입니다.
# 50명의 승객과 매칭 기회가 있을 떄, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1: 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요시간 5 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 6분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [ ] 3번째 손님 (소요시간 : 21분)
# ...
# [O] 50번째 손님 (소요시간 : 10분)

# 총 탑승 승객 : 2 분

# 내 풀이

from random import *

passenger = 0
count_num = 0

while passenger < 50:
    time = randint(5, 51)
    passenger += 1

    if 5 <= time <= 15:
        count_num += 1
        print(f'[O] {passenger}번째 손님 (소요시간 : {time}분)')
        
    elif time > 15:
        print(f'[ ] {passenger}번째 손님 (소요시간 : {time}분)')

print('\n총 탑승 승객 : {} 분'.format(count_num))

# 강의 풀이

# count_num = 0

# for passenger in range(1, 51):
#     time = randrange(5, 51)

#     if 5 <= time <= 15:
#         print(f'[O] {passenger}번째 손님 (소요시간 : {time}분)')
#         count_num += 1
        
#     elif time > 15:
#         print(f'[ ] {passenger}번째 손님 (소요시간 : {time}분)')

# print('\n총 탑승 승객 : {} 분'.format(count_num))