import sys

arr = [[0] * 1001 for _ in range(1001)]
count = [0] * 1001

N = int(sys.stdin.readline())

for color in range(1, N + 1):
    x_start, y_start, x_len, y_len = map(int, sys.stdin.readline().split())

    for y in range(y_start, y_start + y_len):
        arr[y][x_start:x_start + x_len] = [color] * x_len # 해당 범위를 통째로 바꾸기
        # for x in range(x_start, x_start + x_len): # 이 방식보다 빠른 듯
        #     arr[y][x] = color

# 카운팅 정렬 방식으로 세기 : 빠른듯
for i in range(1001):
    for j in range(1001):
        count[arr[i][j]] += 1

for color_2 in range(1, N + 1):
    print(count[color_2])

# for color_2 in range(1, N + 1): 
#     count = 0
#     for i in range(1001):
#         for j in range(1001):  
#             if arr[i][j] == color_2:
#                 count += 1
    # print(count)
