score_b = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
t = int(input())

for tt in range(t):
    n, k = map(int, input().split())

    score_l = []
    for i in range(n):
        mid, fin, hw = map(int, input().split())

        score = mid * 0.35 + fin * 0.45 + hw * 0.2
        score_l.append(score)

    find_score = score_l[k - 1]

    score_l.sort(reverse = True)
    find_index = score_l.index(find_score)

    a = n / 10
    kk = int(find_index // a)
    print(find_index)
    print(kk)
    print(f'#{tt + 1} {score_b[kk]}')
