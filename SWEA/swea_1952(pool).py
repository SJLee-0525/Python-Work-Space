def used(m, expenditure):
    global min_result
    if m >= 12:
        if min_result > expenditure:
            min_result = expenditure
        return

    # 가지치기. 최소값보다 가격이 높아지면 더 돌지 않고 리턴
    if expenditure > min_result:
        return

    else:
        # 이용권 종류별로 순회
        for type in range(4):
            temp_ex = expenditure # 가격 할당
            if type == 0:   # 1일권
                temp_ex += prices[type] * plan[m]
                used(m + 1, temp_ex)
            elif type == 1: # 1달권
                temp_ex += prices[type]
                used(m + 1, temp_ex)
            elif type == 2: # 3달권
                temp_ex += prices[type]
                used(m + 3, temp_ex)
            elif type == 3: # 1년권
                temp_ex += prices[type]
                used(m + 12, temp_ex)


T = int(input())
for tc in range(1, T + 1):
    prices = list(map(int, input().split())) # 1일, 1달, 3달, 1년
    plan = list(map(int, input().split()))   # 12개월 이용 계획

    min_result = 1000001
    used(0, 0)

    print(f'#{tc} {min_result}')