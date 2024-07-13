from random import *

x = []

for i in range(3):
    day = int(randint(4, 28))
    x.append(f'{day}')

    if i == 2:
        x = ', '.join(x)
        print(f'오프라인 스터디 모임 날짜는 매월 {x}일로 선정되었습니다.')