# 입력 받을때 rstrip 안 붙여서 딕셔너리 이용했을 때 오류나는 거였음
# 진짜 어이없넹 문제,

import sys
sys.stdin = open("./sample_input.txt", "r")

# 딕셔너리에 담아서 16진수를 변환하는게 더 빠를 듯
BB = {'0': [0, 0, 0, 0],
      '1': [0, 0, 0, 1],
      '2': [0, 0, 1, 0],
      '3': [0, 0, 1, 1],
      '4': [0, 1, 0, 0],
      '5': [0, 1, 0, 1],
      '6': [0, 1, 1, 0],
      '7': [0, 1, 1, 1],
      '8': [1, 0, 0, 0],
      '9': [1, 0, 0, 1],
      'A': [1, 0, 1, 0],
      'B': [1, 0, 1, 1],
      'C': [1, 1, 0, 0],
      'D': [1, 1, 0, 1],
      'E': [1, 1, 1, 0],
      'F': [1, 1, 1, 1]}

# 각 코드의 비율
C = {'3211': 0,
     '2221': 1,
     '2122': 2,
     '1411': 3,
     '1132': 4,
     '1231': 5,
     '1114': 6,
     '1312': 7,
     '1213': 8,
     '3112': 9}

# 이거 안 쓸 거임. 비율 쓸 거임
# C = {'0001101': 0,
#      '0011001': 1,
#      '0010011': 2,
#      '0111101': 3,
#      '0100011': 4,
#      '0110001': 5,
#      '0101111': 6,
#      '0111011': 7,
#      '0110111': 8,
#      '0001011': 9}

##################################################################################

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N개의 줄, M 가로 길이
    CODE = []
    for _ in range(N):
        init_input = list(input().strip())  # 16진수로 된 코드 한 줄을 입력받고
        R = []
        for ii in init_input:  # 16진수 코드 1줄을 돌면서
            R.extend(BB[ii])  # 2진수로 변환해서 (str에 더하는 방식)
        CODE.append(list(R))  # 한 줄을 통째로 리스트에 담아 저장

    codeset = set()  # 코드들을 담을 set: 중복된 코드를 담지 않기 위해 set 사용
    bin_M = M * 4  # 2진수로된 코드의 가로 길이

    for n in range(N):  # 한 행씩 순회
        temp = []
        op = CODE[n][0]  # 초기 값 할당 (0 또는 1)
        cnt = 0  # 갯수를 셀 변수
        for i in range(bin_M):  # 한 행의 열들을 순회하는데
            cnt += 1  # 하나 갈 때마다 카운트 올림
            if op != CODE[n][i] or i + 1 == bin_M:  # 만약에 지금 op에 저장된 값과 다르거나, 다음이 코드의 끝이라면
                temp.append(cnt)  # 카운트 한 것을 담음
                op = CODE[n][i]  # op 변수 재할당
                cnt = 0  # 카운트 초기화

        # print(temp)
        ''' 출력값 예시: 이런식으로 1과 0이 바뀔 때마다 해당 값의 길이를 측정해서 비율을 담을 수 있음
        # 아래는 0이 770번 나오고 1이 6번, 0이 9번, 1이 3번 이런식으로 나왔단 뜻
        [770, 6, 9, 3, 3, 3, 9, 6, 3, 12, 3, 3, 3, 9, 3, 6, 3, 3, 9, 6, 9, 6, 3, 3, 3, 3, 9, 6, 6, 6, 6, 3, 162, 1, 1, 2, 1, 2, 3, 1, 1, 3, 1, 2, 1, 3, 1, 2, 1, 2, 3, 1, 1, 4, 1, 1, 2, 2, 2, 1, 3, 1, 1, 2, 850]
        [770, 6, 9, 3, 3, 3, 9, 6, 3, 12, 3, 3, 3, 9, 3, 6, 3, 3, 9, 6, 9, 6, 3, 3, 3, 3, 9, 6, 6, 6, 6, 3, 1065]
        [2000] << 얘는 처음부터 끝까지 0인 거임
        '''

        s = 0  # 시작점 지정 (0부터)
        while len(temp) > 32:  # 뽑아온 temp의 길이가 32 이상인 경우에만 시작 (위 예시처럼 [2000]하나면 제낌)
            temp_cd = temp[s:s + 32]  # temp_cd는 temp의 s에서 s+31까지를 잘라서 할당해줌
            # print(1, temp_cd)
            '''1 [770, 6, 9, 3, 3, 3, 9, 6, 3, 12, 3, 3, 3, 9, 3, 6, 3, 3, 9, 6, 9, 6, 3, 3, 3, 3, 9, 6, 6, 6, 6, 3]'''

            std_op = min(temp_cd)  # 비율을 나눠줄 기준 값 할당(temp_cd에서 가장 작은 값)
            for ii in range(1, 32):  # temp_cd의 가장 첫번째 값을 제외한(얘는 어차피 수가 이상함) 나머지를
                temp_cd[ii] = temp_cd[ii] // std_op  # std_op(기준 값)으로 나눠줌
            # print(2, temp_cd)
            '''2 [770, 2, 3, 1, 1, 1, 3, 2, 1, 4, 1, 1, 1, 3, 1, 2, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1, 3, 2, 2, 2, 2, 1]'''

            temp_cd[0] = 7 - sum(temp_cd[1:4])  # 첫번째 값은 temp_cd의 2, 3, 4번째 값을 더한 것에서 빼준 값으로 할당
            # print(3, temp_cd)
            '''3 [1, 2, 3, 1, 1, 1, 3, 2, 1, 4, 1, 1, 1, 3, 1, 2, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1, 3, 2, 2, 2, 2, 1]'''

            codeset.add(''.join(map(str, temp_cd)))  # 완성된 코드를 str으로 합쳐서 삽입
            # print(codeset)
            '''{'12311132141113121132321111322221', '32111132212212133211111411141213', '21221231123121221114311211141312' ... }'''

            s += 32  # 하나 끝내고 나면 s에 32를 더해서 다음 반복 준비해줌
            if s >= len(temp) - 1:  # 만약 더해진 s값이 temp 변수 길이보다 초과되면 반복 중지
                break

    result = 0  # 최종 결과 변수
    for cd in codeset:  # codeset에서 만들어진 암호들을 가져옴
        temp_re = []  # 각 암호마다 결과 값 담을 임시 리스트 생성하고
        for i in range(0, 32, 4):  # 4개씩 끊어서 순회
            temp_re.append(C[cd[i:i + 4]])  # 딕셔너리에서 암호코드를 해석해서 암호르 담음
        # print(cd)       # 12311132141113121132321111322221
        # print(temp_re)  # [5, 4, 3, 7, 4, 0, 4, 1]

        holsu = 0  # 홀수 값 담을 변수
        jjaksu = 0  # 짝수 값 담을 변수
        for i3 in range(7):  # 맨 뒤의 것을 제외한 나머지 7개만 순회
            if i3 % 2 == 0:  # 자릿 수가 홀수면 (인덱스기에 나눠 떨어져야 홀수임)
                holsu += temp_re[i3]  # 홀수 변수에 값 추가
            else:  # 자릿 수가 짝수면
                jjaksu += temp_re[i3]  # 짝수 변수에 값 추가

        temp_result = (holsu * 3) + jjaksu + temp_re[7]  # (홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드가
        if temp_result % 10 == 0:  # 10으로 나누어 떨어지면
            result += sum(temp_re)  # 최종 결과 변수에 해당 암호문에 적혀있는 숫자들의 합 추가

    print(f'#{tc} {result}')  # 출력