import sys

melon = int(sys.stdin.readline())

coord = [tuple(map(int, sys.stdin.readline().split())) for _ in range(6)] # [(4, 50), (2, 160), (3, 30), (1, 60), (3, 20), (1, 100)]

x_list = [x for x in coord if x[0] == 1 or x[0] == 2] # [(2, 160), (1, 60), (1, 100)]
y_list = [y for y in coord if y[0] == 3 or y[0] == 4] # [(4, 50), (3, 30), (3, 20)]

x_value, y_value = max(x_list, key=lambda x:x[1]), max(y_list, key=lambda y:y[1]) # 변의 길이가 가장 큰 것들 뽑고 제거
x, y = x_value[1], y_value[1]
coord.remove(x_value)
coord.remove(y_value) # [(3, 30), (1, 60), (3, 20), (1, 100)]

print(x, y)
print(coord)

xx, yy = coord[1][1], coord[2][1]

print(((x * y) - (xx * yy)) * melon)