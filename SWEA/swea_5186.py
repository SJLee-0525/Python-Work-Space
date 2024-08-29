T = int(input())
for tc in range(1, T + 1):
    FL = input()
    result = []
    if FL[-1] != '5': # 소수 끝자리가 5가 아니면 2진수는 무한소수 발생
        print(f'#{tc} overflow')
    else:
        FL = float(FL) # float 형으로 변환
        while len(result) < 12 and FL > 0: # 결과 길이가 12를 넘어가지 않고, FL이 0이상인 동안
            FL *= 2     # FL에 2를 곱하고
            if FL >= 1: # 1 이상이 되면
                result.append('1') # 결과에 1 추가
                FL -= 1 # 1 빼주고 반복
            else: # 1 미만이면
                result.append('0') # 0 추가하고 반복

        if len(result) <= 12:   # 12줄 이내면 출력
            print(f'#{tc} {"".join(result)}')
        else:                   # 넘어가면 오버플로우
            print(f'#{tc} overflow')