# 65 - 90
# s = list(input())
# n = len(s)
# num_list = []

# for i in s:
#     temp_num = ord(i) - 65
#     if 15 <= temp_num <= 18:
#         num_list.append(8)
#     elif 19 <= temp_num <= 21:
#         num_list.append(9)
#     elif 22 <= temp_num <= 25:
#         num_list.append(10)
#     else:
#         num_list.append(temp_num // 3 + 3)

# print(sum(num_list))
# print(num_list)

# 풀이

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alpha = list(input())
result = 0

for i in alpha:
    for j in dial:
        if i in str(j):
            num = dial.index(j) + 3		
            result += num
            
print(result)