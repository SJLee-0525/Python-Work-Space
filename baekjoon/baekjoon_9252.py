import sys, pprint

strA = sys.stdin.readline().rstrip()
strB = sys.stdin.readline().rstrip()

LCS = [[''] * (len(strB) + 1) for _ in range(len(strA) + 1)]

for a in range(1, len(strA) + 1):
    for b in range(1, len(strB) + 1):
        if strA[a - 1] == strB[b - 1]:
            LCS[a][b] = LCS[a - 1][b - 1] + strA[a - 1]
        else:
            if len(LCS[a - 1][b]) >= len(LCS[a][b - 1]):
                LCS[a][b] = LCS[a - 1][b]
            else:
                LCS[a][b] = LCS[a][b - 1]

# pprint.pprint(LCS)

result = LCS[-1][-1]
print(len(result))

if len(result) != 0:
    print(result)
