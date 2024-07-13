t = int(input())

for tt in range(t):
    n = int(input())
    answer = input()
    submit = input()

    result = 0
    for i in range(n):
        if answer[i] == submit[i]:
            result += 1

    print(f'#{tt + 1} {result}')
