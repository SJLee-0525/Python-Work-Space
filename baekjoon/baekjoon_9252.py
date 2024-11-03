import sys
#import pprint

strA = sys.stdin.readline().rstrip()
strB = sys.stdin.readline().rstrip()

LCS = [[0] * (len(strB) + 1) for  _ in range(len(strA) + 1)]

for a in range(len(strA)):
    for b in range(len(strB)):
        if strA[a] == strB[b]:
            LCS[a + 1][b + 1] = LCS[a][b + 1] + 1
        else:
            LCS[a + 1][b + 1] = max(LCS[a][b + 1], LCS[a + 1][b])

# pprint.pprint(LCS)

stack = []
i, j = len(strA), len(strB)

while i > 0 and j > 0 and LCS[i][j] > 0:
    if LCS[i - 1][j] == LCS[i][j - 1] == LCS[i][j] - 1:
        stack.append(strB[j - 1])
        i -= 1
        j -= 1
    elif LCS[i - 1][j] == LCS[i][j]:
        i -= 1
    elif LCS[i][j - 1] == LCS[i][j]:
        j -= 1

print(LCS[len(strA)][len(strB)])
if LCS[len(strA)][len(strB)] > 0:
    print(''.join(stack[::-1]))
