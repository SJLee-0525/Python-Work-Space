# n = int(input())

# l = list(range(1, n + 1))

# n_l = []
# for i in l:
#     n_l.append(list(map(int, str(i))))

# n_l2 = []
# for j in n_l:
#     ji = ''.join(map(str, j))
#     ji = int(ji)
#     if ji + sum(j) == n:
#         n_l2.append(ji)

# if len(n_l2) == 0:
#     print(0)

# else:
#     print(min(n_l2))


n = int(input())

for i in range(1, n + 1):
    num = sum(map(int, str(i)))
    num_sum = i + num
    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)
