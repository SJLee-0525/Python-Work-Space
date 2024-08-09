# 방법 2 - 시간초과.
import sys
N = int(sys.stdin.readline().rstrip())
final_dic1 = {}
final_list = [0] * N # 색종이별 최종 값을 담을 리스트


for k2 in range(N):
    left_x, left_y, length, height = map(int, sys.stdin.readline().rstrip().split())
    right_x = left_x + length
    right_y = left_y + height
    for i in range(left_x,right_x):
        for j in range(left_y,right_y):
            final_dic1[(i,j)] = k2 # 딕셔너리 어차피 key-value 하나니까 뒤에 입력값으로 덮어쓰기
            
print(final_dic1)
print()
final_dict = {}
for k in range(N):
    left_x, left_y, length, height = map(int, sys.stdin.readline().rstrip().split())
    right_x = left_x + length
    right_y = left_y + height
    final_dict = {(i, j): k for i in range(left_x, right_x) for j in range(left_y, right_y)}
print(final_dict)