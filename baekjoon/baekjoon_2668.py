import sys

def dfs(start):
    now = start

    stack, temp = [], []    # dfs에서 사용할 스택, 해당 루프에서 방문한 숫자를 기록할 temp
    visited = [0] * (N + 1) # 방문 여부 기록: 처음 지점으로 돌아와야 하므로, 시작점에 표시하지 않고 시작

    while 1:
        next = adjN[now]        # 다음 숫자 탐색
        if not visited[next]:   # 다음 숫자를 방문한 적 없다면
            stack.append(now)   # 스택에 현 숫자 push
            temp.append(now)    # 현 숫자 기록
            now = next          # 이동
            visited[now] = 1    # 방문 표시
            if now == start:    # 만약 시작점에 돌아왔다면: 루프 존재
                for t in temp:      # 기록한 숫자를 돌면서 result 배열에 기록 후 리턴
                    result[t] = 1
                return
        else:           # 갈 수 있는 곳이 없다면
            if stack:   # 스택에 숫자가 있다면 뽑음
                now = stack.pop()
            else:       # 없으면 종료
                return

############################################

N = int(sys.stdin.readline())

# 인접 숫자 기록
adjN = [0] * (N + 1)
for i in range(1, N + 1):
    j = int(sys.stdin.readline())
    adjN[i] = j

result = [0] * 101      # 결과 기록할 배열

for i in range(1, N + 1):
    if not result[i]:   # 결과에 기록된 적 없는 숫자라면 dfs 탐색
        dfs(i)

print(sum(result))
for i in range(101):
    if result[i]:
        print(i)