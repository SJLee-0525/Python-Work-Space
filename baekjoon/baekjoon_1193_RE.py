# line = 1

# x = int(input())

# while x > line:
#     x -= line
#     x += 1

# if line % 2 == 0:
#     a = x
#     b = line - x + 1

# elif line % 2 == 1:
#     a = line - x + 1
#     b = x

# print(f'{a}/{b}')

n = int(input())

line = 0
line_end_num = 0

while line_end_num < n:
    line += 1
    line_end_num += line

k = line_end_num - n

if line % 2 == 0:
    a = line - k
    b = k + 1

elif line % 2 == 1:
    a = k + 1
    b = line - k

print(f'{a}/{b}')