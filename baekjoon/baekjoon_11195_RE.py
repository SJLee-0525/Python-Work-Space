def prime(a):
    if a == 0:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

all_list = list(range(2, 1001))
s_list = []

for s in all_list:
    if prime(s):
        s_list.append(s)

print(s_list)

test_n = int(input())

for x in range(test_n):
    num = int(input())

    c = 0
    for a1 in s_list:
        if a1 >= num:
            break
        elif 
    print(c)

