# kg_del = int(input())

# temp_5 = int(kg_del // 5)
# temp_3 = int(kg_del // 3)

# l = []


# for i in range(temp_5 + 1):
#     for j in range(temp_3 + 1):
#         if i * 5 + j * 3 == kg_del:
#             l.append(i + j)
#             break
#         elif i * 5 + j * 3 > kg_del:
#             break

# if len(l) == 0:
#     print(-1)

# elif len(l) > 0:
#     print(min(l))

n = int(input())

if n % 5 == 0:
    print(n // 5)

else:
    c = 0
    while n > 0:
        n -= 3
        c += 1
        if n % 5 == 0:
            print(n // 5 + c)
            break

        elif n == 1 or n == 2:
            print(-1)

        elif n == 0:
            print(c)