for tt in range(1, 11):
    n = int(input())
    building_list = list(map(int, input().split()))

    result = 0
    for i in range(2, n - 2):
        temp_list = [building_list[i - 2], building_list[i - 1], building_list[i + 1], building_list[i + 2]]
        
        if building_list[i] - max(temp_list) > 0:
            result += building_list[i] -max(temp_list)

    print(f'#{tt} {result}')

'==============='
# 내장 함수 없이 풀기
for T in range(1, 11):
    N = int(input())
    building_list = list(map(int, input().split()))
    result = 0

    for i in range(2, N - 2):
        temp_list = [building_list[i - 2], building_list[i - 1], building_list[i + 1], building_list[i + 2]]
        high_building = temp_list[0]

        for temp_building in temp_list:
            if high_building < temp_building:
                high_building = temp_building
        temp_result = building_list[i] - high_building

        if temp_result > 0:
            result += temp_result
    print(f'#{T} {result}')
