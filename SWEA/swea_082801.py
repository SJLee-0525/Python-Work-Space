oper = ['+', '-', '/', '*'] # 연산자 모음

def order(node):
    '''후위 순회'''
    # 만약 해당 정점이 연산자가 아니고, 1 이상의 정수라면 반환
    if tree[node] not in oper and tree[node] > 0:
        return tree[node]
    a = order(LR[0][node])  # 왼쪽 자식이 있다면 왼쪽 탐색 후 a에 할당
    b = order(LR[1][node])  # 오른쪽 자식이 있다면 오른쪽 탐색 후 b 할당
    if tree[node] == '+':   # 연산자에 맞춰서 연산 수행 후 반환
        return a + b
    elif tree[node] == '-':
        return a - b
    elif tree[node] == '*':
        return a * b
    elif tree[node] == '/':
        return a / b

################################################################

for tc in range(1, 11):

    N = int(input())
    LR =[[0] * (N + 1) for _ in range(2)]   # 각 정점의 좌우 자식 정보를 기록
    tree = [0] * (N + 1)                    # 각 정점의 값 기록

    for _ in range(N):  # 정점의 개수만큼 입력 받음
        n, p1, *p2 = input().split()
        n = int(n)
        if p1 in oper:  # 만약 p1이 operator면
            tree[n] = p1 # 해당 정점에 기록
            for p in range(len(p2)):    # operator를 가진 노드는 자식을 가짐
                LR[p][n] = int(p2[p])   # 자식 정보 기록
        else:   # operator가 아니면 정수를 가지고 자식이 없음
            tree[n] = int(p1)   # 해당 정점에 정수 기록

    result = order(1) # 루트: 1로 해서 후위 순회
    print(f'#{tc} {int(result)}') # 소수점 버리고 출력
