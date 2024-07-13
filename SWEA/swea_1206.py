for tt in range(1, 11):
    n = int(input())
    building_list = list(map(int, input().split()))

    result = 0
    for i in range(2, n - 2):
        temp_list = [building_list[i - 2], building_list[i - 1], building_list[i + 1], building_list[i + 2]]
        
        if building_list[i] - max(temp_list) > 0:
            result += building_list[i] -max(temp_list)

    print(f'#{tt} {result}')

