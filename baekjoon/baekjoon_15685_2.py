import sys

def rotateCoord(cx, cy, px, py):
    '''입력받은 cx, cy 좌표를 기준점 px, py를 기준으로 90도 회전'''
    nx = px - (cy - py)
    ny = py + (cx - px)

    return nx, ny

def makeDragonCurve(x, y, d, g):
    '''x, y에서 방향 d로 시작하는 드래곤 커브를 g세대까지 생성'''
    curve = [(x, y), (x + dx[d], y + dy[d])] # 0세대 드래곤 커브 생성

    for gen in range(g):
        px, py = curve[-1] ####### 마지막 좌표가 기준점 px, py

        ###### 기존 커브 좌표들을 거꾸로 순회하면서 회전한 좌표들을 저장
        newCurve = []
        for i in range(len(curve) - 1, -1, -1):
            cx, cy = curve[i]
            newCurve.append(rotateCoord(cx, cy, px, py))

        curve.extend(newCurve)  # 회전한 배열 추가

    return set(curve)           # 중복 제거 후 반환

def countSquare():
    grid = [[0] * 101 for _ in range(101)]

    # 좌표로 옮겨 담기
    for cx, cy in curves:
        grid[cx][cy] = 1

    # 정사각형 카운트
    cnt = 0
    for x in range(100):
        for y in range(100):
            if 1 == grid[x][y] == grid[x + 1][y] == grid[x][y + 1] == grid[x + 1][y + 1]:
                cnt += 1

    return cnt

#############################################################################

N = int(sys.stdin.readline())

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

curves = set()
for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    curves.update(makeDragonCurve(x, y, d, g))

print(countSquare())
