# a, b = input().split()
# num = list(a)
# n = int(b)

# temp_list = []
# SUM = 0

# for i in range(len(num)):
#     temp = ord(num[i])
#     if temp <= 57:
#         temp -= 48
#         temp_list.append(temp)
#     else: 
#         temp -= 55
#         temp_list.append(temp)

# for i in range(len(temp_list)):
#     SUM += temp_list[i] * (n ** (len(temp_list) - (i + 1)))

# print(SUM)


num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = input().split()
n = n[::-1]

answer = 0

for i, num in enumerate(n):
    answer += (int(b) ** i) * num_list.index(num)

print(answer)