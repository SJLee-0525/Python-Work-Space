import sys

inputSound = list(sys.stdin.readline().rstrip())

resultSound = [-1] * len(inputSound)
temp = [0] * (len(inputSound) // 5)
duckSound = ['q', 'u', 'a', 'c', 'k']

for s in range(len(inputSound)):
    for t in range(len(temp)):
        if inputSound[s] == duckSound[temp[t]]:
            inputSound[s] = t
            resultSound[s] = 0
            temp[t] = (temp[t] + 1) % 5
            break

if sum(temp) == 0 and sum(resultSound) == 0:
    print(max(inputSound) + 1)
else:
    print(-1)