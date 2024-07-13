n = int(input())


n_list = list(map(int, input().split()))

n_list.sort()
md_n = (n // 2) + 1

print(n_list[md_n - 1])