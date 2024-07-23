# 투포인터

def trap(ground): 
    if not ground:
        return 0
    
    volume = 0
    left, right = 0, len(ground) - 1 # left는 0번부터, right는 -1부터
    left_max, right_max = ground[left], ground[right] # max 값을 일단 할당

    while left < right: # 둘이 만나는 것 방지
        left_max, right_max = max(ground[left], left_max), max(ground[right], right_max)
        # 현재 위치와, 이전의 max 값을 비교 후 max 값을 재할당

        if left_max <= right_max: # 좌우 어느쪽이던 낮은쪽은 높은쪽으로
            volume += left_max - ground[left] # max 값과 차이만큼 볼륨 증가
            left += 1 # 이동
        else:
            volume += right_max - ground[right]
            right -= 1

    return volume

def trap_2(ground_list):
    left_index, right_index = 0, len(ground_list) - 1
    left_max, right_max = 0, 0
    rain_sum = 0
    
    while left_index <= right_index:
        left, right = ground_list[left_index], ground_list[right_index]
        left_max, right_max = max(left, left_max), max(right, right_max)

        if left_max <= right_max:
            rain_sum += left_max - left
            left_index += 1

        else:
            rain_sum += right_max - right
            right_index -= 1

    return rain_sum


ground = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(ground))